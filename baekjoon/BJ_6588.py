# 내 풀이
import sys


def goldbach(n):
    for i in range(3, n, 2):
        if isPrime(i) and isPrime(n-i):
            return i, n-i
        else:
            print("Goldbach's conjecture is wrong.")


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

# 2 다른 사람 풀이(시간 더 적게 걸림)


def Goldbach():
    check = [False, False] + [True] * 1000000
    for i in range(2, 1001):
        if check[i] == True:
            for j in range(i + i, 1000001, i):
                check[j] = False
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        A = 0
        B = n
        for _ in range(1000000):
            if check[A] and check[B]:
                print(f"{n} = {A} + {B}")
                break
            A += 1
            B -= 1
        else:
            print("Goldbach's conjecture is worng.")


Goldbach()
