import codecs
import csv
import json


def utf_8_encoder(unicode_csv_data):
    """
    Encodes to UTF-8
    """
    for line in unicode_csv_data:
        encoded = line.encode('utf-8')
        yield encoded


def csv_to_jsonlines(infile):
    """
    Loads the CSV data as JSON
    """
    with codecs.open(infile, 'rU', encoding='iso8859_15') as csv_file:
        outfile = infile + '.jsonlines'
        csv_reader = csv.DictReader(utf_8_encoder(csv_file))
        with open(outfile, 'w') as json_file:
            for row in csv_reader:
                json.dump(row, json_file)
                json_file.write('\n')
        return outfile
