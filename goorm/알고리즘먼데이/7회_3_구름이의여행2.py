# 맞음
from collections import deque


def bfs():
    while queue:
        curr = queue.popleft()
        if curr == K and visited[K]:
            return visited[K]
        for i in graph[curr]:
          if not visited[i]:
            visited[i] = visited[curr] + 1
            queue.append(i)
    return -1


N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
queue = deque()
queue.append(K)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
print(bfs())
