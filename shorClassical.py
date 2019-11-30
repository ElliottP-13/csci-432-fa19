import random


def power(a, b):  # To avoid overflow error, we calculate the 'slow way'
    z = 1
    for i in range(int(b)):
        z *= a
    return z


def euclid(a, b):  # Implements Euclid's algorithm for GCD
    while a != 0:
        temp = a
        a = b % a
        b = temp
    return b


def findPeriod(g, N):  # Finds the period of f(x)= g^x % N
    i = 0
    repeat = (g**(i)) % N  # The number we are looking for
    r = -1
    z = g**i  # the current number we are checking, ie. g^x
    while r != repeat:  # until we find the number, keep increasing x
        i += 1
        z *= g  # increments the exponent: z = g^i --> z = g^(i+1)
        r = z % N
    return i


p = -1  # initializes our variables
N = 314191  # the number we are factoring
g = 2
while p % 2 != 0:
    g = random.randint(3, N-2)  # guess a random number
                                # the range limits the factors to not be 1 or N

    if euclid(g, N) == 1:  # if we didn't guess a factor improve our guess
        print("Finding period")
        p = findPeriod(g, N)
        print("WE FOUND: " + str(p))
    else:
        print("we guessed a factor")
        break

if p == -1:  # We guessed a factor so p was never updated
    a = float(euclid(g, N)) # We float them just so they are consistent
    b = float(N / a)
else:
    print("PERIOD: " + str(p))
    print("GUESS: " + str(g))
    num = power(g, p/2)
    a = euclid(num + 1, N)
    b = euclid(num - 1, N)

print(a)
print(b)
