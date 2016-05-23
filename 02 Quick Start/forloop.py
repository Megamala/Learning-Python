#! C:\Python31\python

fh = open('lines.txt')
for line in fh.readlines():
    print(line, end=' ')
