import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    cnt = 0
    queue = deque([n])
    visited = [0 for _ in range(N + 1)]
    while queue:
        temp = queue.popleft()
        visited[temp] = 1
        cnt += 1
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
res_arr = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
for i in range(1, N + 1):
    res_arr[i] = bfs(i)
    print(res_arr)
for i in range(1, N + 1):
    if res_arr[i] == max(res_arr):
        print(i, end=" ")
