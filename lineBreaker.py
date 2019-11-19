import os
from glob import iglob
import math


def findFirst(s, start):
    one = s.find(',', start) + 1
    two = s.find('.', start) + 1
    three = s.find(';', start) + 1
    if one == 0:
        one = len(s)
    if two == 0:
        two = len(s)
    if three == 0:
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
                arr.append(line[lastIndx:indx].strip())
                lastIndx = indx

                run = indx < len(line) - 5

        fileTest.close()

        fileWrite = open(path, 'w')
        writeStr = "\n".join(arr)
        fileWrite.write(writeStr)
        fileWrite.close()
