# http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000176&itemidx=1&sign=42881919403184543ad80cb756f279ab
import urllib.request
import pickle
import os

def urlRead(urlstring):
    if urlstring.__len__() > 1:
        requesthandle = urllib.request.urlopen(urlstring)
        requeststring = requesthandle.read().decode('utf-8')
        return requeststring

def stringSplitToList(starget, ssplit = ","):
    if starget:
        list1 = []
        for s1 in starget.split(ssplit):
            list1.append(s1)
    return list1

def listSplitToDict(ltarget, ssplit = "|"):
    if ltarget:
        dict1 ={}
        for s1 in ltarget:
            s1split = s1.split(ssplit)
            if s1split.__len__() == 2:
                dict1[s1split[0]] = s1split[1]
        return dict1

citynumberdatafile = r".\citynumber.db"
if not os.path.exists(citynumberdatafile):
    print('正在读取城市代码...')
    dcitynumber = {}
    dprovinces = listSplitToDict(stringSplitToList(urlRead("http://m.weather.com.cn/data5/city.xml")))
    for province in dprovinces:
        dprovincecities = listSplitToDict(stringSplitToList(urlRead("http://m.weather.com.cn/data5/city"+province+".xml")))
        for city in dprovincecities:
            dcounties = listSplitToDict(stringSplitToList(urlRead("http://m.weather.com.cn/data5/city"+city+".xml")))
            for county in dcounties:
                dcitynumber[dcounties[county]] = county
    hfile = open(citynumberdatafile, "wb")
    pickle.dump(dcitynumber, hfile)
    hfile.close()

if os.path.exists(citynumberdatafile):
    hfile = open(citynumberdatafile, "rb")
    dcitynumber = pickle.load(hfile)
    hfile.close()
    print(dcitynumber)

print(urlRead("http://www.weather.com.cn/adat/cityinfo/101"+dcitynumber['拉萨']+".html"))
