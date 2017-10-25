import sys
import csv
import json

if __name__ == '__main__':
    fn = sys.argv[1]
    with open(fn) as f:
        with open(fn + '.jsonlines', 'w') as o:
            reader = csv.DictReader(f)
            for row in reader:
                d = dict(row)
                o.write(json.dumps(d) + '\n')
