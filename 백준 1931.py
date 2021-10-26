N = int(input())
info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append([start, end])
info.sort(key=lambda x: (x[0], x[1]))
for i in info:
