import sys
input = sys.stdin.readline
N = int(input())
coord = []
for _ in range(N):
    coord.append(list(map(int, input().split())))
coord.sort(key=lambda x: (x[0], x[1]))
for i in coord:
    print(i[0], i[1])
