# 1
#import time

import sys
input = sys.stdin.readline

#start = time.time()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
visited = set()

def solve(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C or board[nx][ny] in visited:
            continue
        visited.add(board[nx][ny])
        solve(nx, ny, cnt + 1)
        visited.remove(board[nx][ny])

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]  # input()으로 했을때 시간초과
#board = [input() for _ in range(R)]  # input()으로 했을때 시간초과
visited.add(board[0][0])
solve(0, 0, 1)
print(ans)

#end = time.time()
#print(end - start)

# 2
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
visited = [False for _ in range(26)]

def solve(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C or visited[board[nx][ny]]:
            continue
        visited[board[nx][ny]] = True
        solve(nx, ny, cnt + 1)
        visited[board[nx][ny]] = False

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - ord("A"), input().strip())) for _ in range(R)]
visited[board[0][0]] = True
solve(0, 0, 1)
print(ans)
