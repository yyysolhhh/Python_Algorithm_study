import sys
input = sys.stdin.readline
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

tshirt = sum([(i // T + 1) if i % T else (i // T) for i in size])
#for i in size:
#    if i % T:
#        tshirt += i // T + 1
#    else:
#        tshirt += i // T

print(tshirt)
print(N // P, N % P)

