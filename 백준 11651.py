import sys
input = sys.stdin.readline
N = int(input())
coord = []
for _ in range(N):
    coord.append(list(map(int, input().split())))
for i in sorted(coord, key=lambda x: (x[1], x[0])):
    print(*i)
