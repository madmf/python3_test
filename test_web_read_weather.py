import urllib.request

def urlRead(urlstring):
    if urlstring.__len__() > 1:
        requesthandle = urllib.request.urlopen(urlstring)
        requeststring = requesthandle.read().decode('utf-8')
        return requeststring

def stringSplitToList(starget, ssplit = ","):
    if starget:
        dict1 = []
        for s1 in starget.split(ssplit):
            dict1.append(s1)
    return dict1

url = "http://www.weather.com.cn/adat/cityinfo/101010100.html"
url = "http://m.weather.com.cn/data5/city.xml"
print(stringSplitToList(urlRead(url)))

# http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000176&itemidx=1&sign=42881919403184543ad80cb756f279ab


