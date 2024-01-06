import sys
from collections import deque


def bfs():
    queue = deque([1])
    comeback = 0
    temp_path = [1]
    while queue:
        curr = queue.popleft()
        for n in graph[curr]:
            if n == N:
                comeback = 1
            if comeback == 0:
                if visited[n] == 0 and n > curr:
                    visited[n] = visited[curr] + 1
                    queue.append(n)
            else:
                if visited[n] == 0 and n < curr:
                    visited[n] = visited[curr] + 1
                    queue.append(n)


input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
path = []
while True:
    P, Q = map(int, input().split())
    if P == Q == 0:
        break
    graph[P].append(Q)
    graph[Q].append(P)
bfs()
print()
