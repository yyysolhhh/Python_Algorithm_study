import sys


def goldbach(n):
    for i in range(3, n, 2):
        if isPrime(i) and isPrime(n-i):
            return i, n-i


def isPrime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True


while(1):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print("%d = %d + %d" % (n, goldbach(n)[0], goldbach(n)[1]))
