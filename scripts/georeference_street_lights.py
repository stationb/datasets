import json

ADDRESS_POINTS_FILE = '../oakland/out/address_points.jsonlines'
STREET_LIGHTS_FILE = '../oakland/out/street_lights.jsonlines'
STREET_LIGHTS_GEO_FILE = '../oakland/out/street_lights_geo.jsonlines'

if __name__ == '__main__':
    with open(STREET_LIGHTS_GEO_FILE, 'w') as slg_file:
        with open(STREET_LIGHTS_FILE, 'r') as sl_file:
            with open(ADDRESS_POINTS_FILE, 'r') as ap_file:
                aps = {}
                for ap in ap_file.readlines():
                    address_point = json.loads(ap)
                    key = '%s %s %s' % (
                        address_point['properties']['street_number'],
                        address_point['properties']['street_name'],
                        address_point['properties']['street_suffix']
                    )
                    aps[key] = address_point['geometry']
                for sl in sl_file.readlines():
                    street_light = json.loads(sl)
                    street_address = '%s %s' % (
                        street_light['properties']['street_number'],
                        street_light['properties']['street_name']
                    )
                    street_light['geometry'] = aps.get(street_address, None)
                    if street_light['geometry']:
                        slg_file.write(json.dumps(street_light))
                        slg_file.write('\n')
