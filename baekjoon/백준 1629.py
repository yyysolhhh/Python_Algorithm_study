import sys
# sys.setrecursionlimit(10000)   # 재귀 한도를 10000까지 풀어줌
input = sys.stdin.readline

# Divide and Conquer (분할정복)


def DnC(a, b):
    if b == 1:
        return a % C
    temp = DnC(a, b//2)
    if b % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * a % C


A, B, C = map(int, input().split())
print(DnC(A, B))
