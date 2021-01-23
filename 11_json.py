import urllib.request
import json

def pretty_print(theJSON):
    print(json.dumps(theJSON, indent=4, sort_keys=True))

def printResults(data):
    #load json object
    theJSON = json.loads(data)
    #print(json.dumps(theJSON, indent=4, sort_keys=True))

    if 'associate' in theJSON['producttypes']:
        pretty_print(theJSON['producttypes'])

def main():
    urlData = 'https://earthquake.usgs.gov/fdsnws/event/1/application.json'

    webUrl = urllib.request.urlopen(urlData)
    print('http stat:', str(webUrl.getcode()))

    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print('Received error')

main()