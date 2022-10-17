from collections import deque


def bfs():
    queue = deque([1])
    island[1] = 0
    while queue:
        curr = queue.popleft()
        for next in Map[curr]:
            if island[next] == -1:
                island[next] = island[curr] + 1
                queue.append(next)


N, M, K = map(int, input().split())
Map = [[] for _ in range(N + 1)]
island = [-1 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    Map[u].append(v)
    Map[v].append(u)
bfs()
if -1 < island[N] <= K:
    print("YES")
else:
    print("NO")
