import sys
input = sys.stdin.readline


def checkPrimeNum(n):
    primeNumList = []
    for i in range(2, n+1):
        divi = 0
        for j in range(1, i+1):
            if i % j == 0:
                divi += 1
        if divi == 2:
            primeNumList.append(i)
    return primeNumList


T = int(input())
N = [int(input()) for _ in range(T)]
primeNum = checkPrimeNum(max(N))
for i in N:
    goldbachPartition = 0
    for j in range(2, i//2+1):
        if j in primeNum and i-j in primeNum:
            goldbachPartition += 1
            # print(j, i-j, end='|')
    print(goldbachPartition)
