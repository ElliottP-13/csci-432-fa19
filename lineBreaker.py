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

x = "ab,cdef.ghij,klmnopqrst,uwxyz"
print(findFirst(x, 0))
print(findFirst(x, 5))
print(findFirst(x, 14))

fileTest = open('demo.tex', 'r')
arr = []
for line in fileTest:
    for i in range(0, len(line), 80):
        arr.append(line[i: i + 80].strip())
print(arr)

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
                print(str(indx-lastIndx))
                arr.append(line[lastIndx:indx])
                lastIndx = indx

                run = indx < len(line) - 5

        fileTest.close()

        fileWrite = open(path, 'w')
        writeStr = "\n".join(arr)
        print(writeStr)
        fileWrite.write(writeStr)
        fileWrite.close()


# for path in file_list:
#     if path.endswith(".tex"):
#         print()
#         print(path)
#         path.strip()
#         infile = open(path, 'r')
#         outfile = open(path, 'w')
#         writeME = ""
#         for line in infile:
#             print(line)
#             if len(line) > 80:
#                 writeME = writeME + ('\n'.join(line[i:i + 80] for i in range(0, len(line), 80)))
#                 print(writeME)
#             else:
#                 writeME = writeME + line
#         outfile.write(writeME)