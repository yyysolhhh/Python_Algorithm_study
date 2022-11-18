# 틀림 (room order 잘못됨)
from collections import deque


def bfs():
    while queue:
        curr, time = queue.popleft()
        print(curr, room_order, visited)
        if curr == N:
            return visited[N]
        for i, t in graph[curr]:
            if len(room_order) > 1:
                if room_order[-2] % A[curr] == i % A[curr]:
                    visited[i] = visited[curr] + t
                    room_order.append(i)
                    queue.append((i, t))
            else:
                visited[i] = visited[curr] + t
                room_order.append(i)
                queue.append((i, t))
    return -1


N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
room_order = [1]
queue = deque([(1, 0)])
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
print(bfs())
