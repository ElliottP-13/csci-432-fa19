import random


def power(a, b):
    z = 1
    for i in range(int(b)):
        z *= a
    return z


def euclid(a, b):
    while a != 0:
        temp = a
        a = b % a
        b = temp
    return b


def findPeriod(g, N):
    i = 0
    repeat = (g**(i)) % N
    r = -1
    z = g**i
    while r != repeat:
        i += 1
        z *= g
        # r = (g**(i + 1)) % N
        r = z % N
    return i


p = -1
N = 314191
g = 2
while p % 2 != 0:
    g = random.randint(3, N-2)

    if euclid(g, N) == 1:
        print("Finding period")
        p = findPeriod(g, N)
        print("WE FOUND: " + str(p))
    else:
        print("we guessed a factor")
        break

if p == -1:
    a = float(euclid(g, N))
    b = float(N / a)
else:
    print("PERIOD: " + str(p))
    print("GUESS: " + str(g))
    num = power(g, p/2)
    a = euclid(num + 1, N)
    b = euclid(num - 1, N)

print(a)
print(b)
