import sys
input = sys.stdin.readline

# 1 - 시간초과
ROOT = 1
N = int(input())
lc = [0 for _ in range(N + 1)]
rc = [0 for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    lc[a] = b
    rc[a] = c
    par[b] = a
    par[c] = a

last = ROOT
while rc[last] != -1:
    last = rc[last]

cur = ROOT
ans = -1
visited = [False for _ in range(N + 1)]
while True:
    visited[cur] = True
    ans += 1
    if lc[cur] != -1 and not visited[lc[cur]]:
        cur = lc[cur]
    elif rc[cur] != -1 and not visited[rc[cur]]:
        cur = rc[cur]
    else:
        if cur == last:
            break
        cur = par[cur]
print(ans)


# 2
N = int(input())
lc = [0 for _ in range(N + 1)]
rc = [0 for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    lc[a] = b
    rc[a] = c
    par[b] = a
    par[c] = a

K = 0
last = 1
while rc[last] != -1:
    last = rc[last]
    K += 1
print(2 * (N - 1) - K)
