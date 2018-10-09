import json
import datetime


with open('jsonFile.json') as readFile:
    data = json.load(readFile)
    for item in data['main']:
        if item['team'] == "Inter":
            #update
            item['comment'] = "bla bla bla"
            item['date'] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")

with open('jsonFile.json', 'w') as writeFile:
    json.dump(data, writeFile, indent=4, sort_keys=True, separators=(',', ': '))

