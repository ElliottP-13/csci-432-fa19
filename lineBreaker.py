import os
from glob import iglob
import math


def findFirst(s, start):
    one = s.find(',', start)
    two = s.find('.', start)
    three = s.find(';', start)
    if one == -1:
        one = len(s)
    if two == -1:
        two = len(s)
    if three == -1:
        three = len(s)

    return min(one, two, three)


# This will return absolute paths
file_list = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]

for path in file_list:
    if path.endswith('.tex'):
        print(path)
        fileTest = open(path, 'r')
        arr = []
        for line in fileTest:
            run = True
            lastIndx = 0
            while run:
                indx = findFirst(line, lastIndx + 80)
                arr.append(line[lastIndx:indx])
                lastIndx = indx + 1

                run = indx < len(line) - 5

        fileTest.close()

        fileWrite = open(path, 'w')
        writeStr = "\n".join(arr)
        fileWrite.write(writeStr)
        fileWrite.close()
