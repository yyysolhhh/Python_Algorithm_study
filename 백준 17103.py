import sys
input = sys.stdin.readline


def primeNum(n):
    divi = 0
    for i in range(1, n+1):
        if n % i == 0:
            divi += 1
    if divi == 2:
        return True
    else:
        return False


T = int(input())
for _ in range(T):
    N = int(input())
    goldbachPartition = 0
    for i in range(1, N//2+1):
        if primeNum(i):
            if primeNum(N-i):
                goldbachPartition += 1
                print(i, N-i, end='|')
    print(goldbachPartition)
