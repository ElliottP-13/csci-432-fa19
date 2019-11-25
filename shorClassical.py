import random
import math

def euclid(a, b):
    if a == 0:
        return b

    return euclid(b % a, a)


def findPeriod(g, N):
    i = 1
    repeat = math.pow(g, i) % N
    r = -1
    while r != repeat:
        i += 1
        r = g**(i + 1) % N
    return i

p = -1
N = 21
g = 2
while p % 2 != 0:
    g = random.randint(3, N-2)

    if euclid(g, N) == 1:
        p = findPeriod(g, N)
    else:
        print("we guessed a factor")
        break

if p == -1:
    a = float(euclid(g, N))
    b = float(N / a)
else:
    print("PERIOD: " + str(p))
    print("GUESS: " + str(g))
    a = euclid(g ** (p/2) + 1, N)
    b = euclid(g ** (p/2) - 1, N)

print(a)
print(b)