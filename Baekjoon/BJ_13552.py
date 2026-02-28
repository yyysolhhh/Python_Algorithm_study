import sys
input = sys.stdin.readline
N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
for _ in range(M):
    x, y, z, r = map(int, input().split())
    ans = 0
    for cx, cy, cz in coords:
        if (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2 <= r ** 2:
            ans += 1
    print(ans)
