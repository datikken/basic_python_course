import urllib.request

def main():
    webUrl = urllib.request.urlopen('https://www.google.com')
    print('http request status: ' + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)

main()