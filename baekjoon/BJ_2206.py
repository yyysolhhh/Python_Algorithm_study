from collections import deque
import copy
import sys

from sqlalchemy import INTEGER

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def print_map_for_test(map):
    for i in map:
        print(i)
    print()


def bfs(map):
    queue = deque([(1, 1)])
    while queue:
        y, x = queue.popleft()
        print(queue, y, x)
        if y == M and x == N:
            print("!")
            return map[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= M < M and map[ny][nx] == 0:
                map[ny][nx] = map[y][x] + 1
                print_map_for_test(map)
                queue.append((ny, nx))


def break_wall():
    ans = float('inf')
    print(ans)
    temp_map = copy.deepcopy(board)
    # print_map_for_test(temp_map)
    for i, row in enumerate(temp_map):
        for j, col in enumerate(row):
            if col == 1:
                temp_map[i][j] = 0
                print_map_for_test(temp_map)
                ans = min(ans, bfs(temp_map))
                temp_map[i][j] = 1
    return (ans)


input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, list(input().rstrip()))))
print(break_wall())
