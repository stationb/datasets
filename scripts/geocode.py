import json
import logging
import os
import requests

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY_STATIONB']


def _get_coords(address, key=GOOGLE_API_KEY):
    req = \
        'https://maps.googleapis.com/maps/api/geocode/json?' \
        'address=%s&' \
        'key=%s' % \
        (address, key)
    res = requests.get(req).json()
    results = res.get('results', None)
    if results:
        top_result = results[0]
        coords = top_result['geometry']['location']
        return [coords['lng'], coords['lat']]
    else:
        return None


def geocode(filename_in, filename_out):
    with open(filename_in, 'rb') as f_in:
        with open(filename_out, 'wb') as f_out:
            counter = 0
            for row in f_in:
                print('Geocoding row: %d' % counter)
                row = json.loads(row)
                street_number = row.get('STNO').strip()
                street_name = row.get('STREET_NAM').strip()
                if street_number and street_name:
                    address = '%s %s, Oakland, CA' % (street_number, street_name.title())
                    coords = _get_coords(address)
                    if coords:
                        row_out = {
                            "properties": row,
                            "geometry": {
                                "type": "Point",
                                "coordinates": coords
                            }
                        }
                        f_out.write(json.dumps(row_out))
                        f_out.write('\n')
                counter += 1


if __name__ == '__main__':
    geocode(
        filename_in='../oakland/in/street_lights.jsonlines',
        filename_out='../oakland/in/street_lights_geo.jsonlines'
    )
