N, M = map(int, input().split())
floor = []
ans = 0
for _ in range(N):
    floor.append(input())
for i in floor:
    for j in range(len(i)):
