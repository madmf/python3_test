import urllib.request

def urlRead(urlstring):
    if urlstring.__len__() > 1:
        requesthandle = urllib.request.urlopen(urlstring)
        requeststring = requesthandle.read().decode('utf-8')
        return requeststring

url = "http://www.baidu.com"
print(urlRead(url))

