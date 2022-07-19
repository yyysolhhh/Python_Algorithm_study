from collections import deque
import sys

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 시간 초과
# def bfs(map):
#     queue = deque([(0, 0)])
#     temp_map = copy.deepcopy(map)
#     while queue:
#         y, x = queue.popleft()
#         if y == N - 1 and x == M - 1:
#             return temp_map[y][x]
#         for i in range(4):
#             ny, nx = y + dy[i], x + dx[i]
#             if 0 <= ny < N and 0 <= nx < M and temp_map[ny][nx] == 0:
#                 temp_map[ny][nx] = temp_map[y][x] + 1
#                 queue.append((ny, nx))
#     return -1


# def break_wall():
#     ans = float('inf')
#     temp_map = copy.deepcopy(board)
#     for i, row in enumerate(temp_map):
#         for j, col in enumerate(row):
#             if col == 1:
#                 temp_map[i][j] = 0
#                 l = bfs(temp_map)
#                 if l != -1:
#                     ans = min(ans, l)
#                 temp_map[i][j] = 1
#     if ans == float('inf'):
#         return -1
#     return (ans + 1)

def bfs():
    queue = deque([(0, 0, 0)])
    visited = [[[0 for z in range(2)] for i in range(M)]
               for j in range(N)]
    w = 0
    while queue:
        y, x, w = queue.popleft()
        if y == N - 1 and x == M - 1:
            return visited[y][x][w] + 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                # 벽 안부수고 이동 (현재 벽이 아니고, 아직 방문 전)
                if board[ny][nx] == 0 and visited[ny][nx][w] == 0:
                    visited[ny][nx][w] = visited[y][x][w] + 1
                    queue.append((ny, nx, w))
                # 벽 부수고 이동 (현재 벽이고, 아직 벽 부순적 없음)
                elif board[ny][nx] == 1 and w == 0:
                    visited[ny][nx][w + 1] = visited[y][x][w] + 1
                    queue.append((ny, nx, w + 1))
    return -1


input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, list(input().rstrip()))))
print(bfs())
