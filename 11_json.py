import urllib.request
import json

def pretty_print(theJSON):
    print(json.dumps(theJSON, indent=4, sort_keys=True))

def printResults(data):
    #load json object
    theJSON = json.loads(data)
    #print(json.dumps(theJSON, indent=4, sort_keys=True))

    if 'title' in theJSON['metadata']:
        pretty_print(theJSON['metadata']['title'])
    for i in theJSON['features']:
        print(i['properties']['place'])
    print('--------------------------')

    for i in theJSON['features']:
        if i['properties']['mag'] >= 6.0:
            print("%2.1f" % i['properties']['mag'], i['properties']['place'], '* AHTUNG')

def main():
    urlData = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02'

    webUrl = urllib.request.urlopen(urlData)
    print('http stat:', str(webUrl.getcode()))

    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print('Received error')

main()