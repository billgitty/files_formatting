import csv
import json

filename = open('crimes2006.csv', 'r')
jsonfile = open('test.json', 'w')


fieldnames = ('cdatetime','address','district','beat','grid','crimedescr','ucr_ncic_code','latitude','longitude')
reader = csv.DictReader(filename, fieldnames)

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

jsonfile.close()