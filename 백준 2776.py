import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    su1 = set(map(int, input().split()))
    M = int(input())
    su2 = list(map(int, input().split()))
    for i in su2:
        if i in su1:
            print(1)
        else:
            print(0)
