
target = r".\test.txt"
string = """
1
2
3
4
5
666~~~

"""

hTargetFile = open(target, "w")
hTargetFile.write(string)
hTargetFile.close()

hTargetFile = open(target)
lineNumber = 0
while True:
    line = hTargetFile.readline()
    if len(line) == 0:
        break
    lineNumber += 1
    print(str(lineNumber) + " --> " + line)
hTargetFile.close()
