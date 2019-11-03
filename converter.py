import io

test = "achour.3 fc:33:42:10:90:30\nD'Avanzo.1 fc:33:42:12:60:20\ndiago.2 fc:33:42:12:60:20\npetzev.2 fc:33:42:12:60:20"
count = test.count('\n')
i = 0
buf = io.StringIO(test)
while (i < count):
    dict={}
    line = buf.readline()
    line.rsplit()
    list = line.split(' ', 2)
    print(list)
    first = list[0]
    print(first)
    #print(first)
    i = i+1


print(buf.readline())