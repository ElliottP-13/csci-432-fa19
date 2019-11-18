import os
from glob import iglob


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

rootdir_glob = 'C:/Users/sid/Desktop/test/**/*' # Note the added asterisks
# This will return absolute paths
file_list = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]

test = "Hello, world..., ohelp; ,.; word"

for path in file_list:
    if path.endswith(".tex"):
        file = open(path, 'r')
        writeString = ""
        for line in file:
            indx = 0
            for i in range(int(len(line)/80)):
                indx = findFirst(line, indx)

                if indx == -1:
                    break

                line = line[:indx] + '\n' + line[:indx]
            writeString += line + '\n'

        writeFile = open(path, 'w')
        writeFile.write(writeString)

