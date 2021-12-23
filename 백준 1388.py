N, M = map(int, input().split())
floor = []
ans = 0
for _ in range(N):
    floor.append(input())
for i in range(len(floor)):
    for j in range(len(i)):
        if floor[i][j] == '-':
            if floor[i][j-1] == '-':
                ans += 0
            else:
                ans += 1
        elif floor[i][j] == '|':
