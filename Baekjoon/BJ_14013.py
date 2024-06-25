import sys

input = sys.stdin.readline
x, y = map(float, input().split())
A = y / x
B = x / y
N = int(input())
for _ in range(N):
    z, q = input().split()
    if q == 'A':
        print(float(z) * A)
    elif q == 'B':
        print(float(z) * B)

