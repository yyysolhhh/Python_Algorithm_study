import sys
input = sys.stdin.readline
N = int(input())
points = []
for _ in range(N):
    points.append(tuple(map(int, input().split())))

# 1 - 시간초과
dist = 1000000000
for k in range(1, N - 1):
    temp = 0
    x, y = points[0]
    for i, j in points[1:k] + points[k + 1:]:
        temp += abs(i - x) + abs(j - y)
        x, y = i, j
    dist = min(dist, temp)
print(dist)


# 2
def distance(a, b):
    return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])

max_diff = -float("inf")
ans = 0
total_dist = sum(distance(i + 1, i) for i in range(N - 1))
for i in range(1, N - 1):
    sm = distance(i, i - 1)
    me = distance(i + 1, i)
    se = distance(i + 1, i - 1)
    diff = sm + me - se
    max_diff = max(max_diff, diff)
print(total_dist - max_diff)
