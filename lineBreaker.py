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


# This will return absolute paths
file_list = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]

fileTest = open('project\part3\part3.tex', 'r')
for line in fileTest:
    print(line)

for path in file_list:
    if path.endswith(".tex"):
        print()
        print(path)
        path.strip()
        infile = open(path, 'r')
        outfile = open(path, 'w')
        writeME = ""
        for line in infile:
            print(line)
            if len(line) > 80:
                writeME = writeME + ('\n'.join(line[i:i + 80] for i in range(0, len(line), 80)))
                print(writeME)
            else:
                writeME = writeME + line
        outfile.write(writeME)