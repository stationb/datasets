import sys
import csv
import json

if __name__ == '__main__':
    fn = sys.argv[1]
    with open(fn) as f:
        with open(fn + '.jsonlines', 'w') as o:
            reader = csv.DictReader(f)
            counter = 1
            for row in reader:
                d = dict(row)
                d['objectid'] = counter
                o.write(json.dumps(d) + '\n')
                counter += 1
