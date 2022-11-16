# 틀림
from collections import deque


def bfs():
    cnt = 1
    queue = deque([1])
    visited[1] = 1
    while queue:
        curr = queue.popleft()
        for i in graph[curr]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                queue.append(i)
    return cnt


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(bfs())
