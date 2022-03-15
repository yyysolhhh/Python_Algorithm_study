from collections import deque
N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N+1)]

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1


def bfs(start):
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for w in range(len(graph[start])):
            if graph[v][w] == 1 and w not in visited:
                visited.append(w)
                queue.append(w)


def dfs(start, visited=[]):
    visited.append(start)
    print(start, end=' ')
    for w in range(len(graph[start])):
        if graph[start][w] == 1 and w not in visited:
            dfs(w, visited)


dfs(V)
print()
bfs(V)
