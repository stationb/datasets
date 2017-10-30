import json
import sys


if __name__ == '__main__':
    fn = sys.argv[1]
    with open(fn) as f:
        with open(fn + '.jsonlines', 'w') as o:
            data = json.load(f)
            counter = 1
            for feature in data['features']:
                feature['properties']['objectid'] = counter
                o.write(json.dumps(feature) + '\n')
                counter += 1
