import pickle

picklefile = r".\picklefile.db"
alist = range(1000)
hpicklefile = open(picklefile, "wb")

pickle.dump(alist, hpicklefile)
hpicklefile.close()

hpicklefile = open(picklefile, "rb")
loadlist = pickle.load(hpicklefile)
hpicklefile.close()
print(loadlist)

for i in loadlist:
    print(i)
