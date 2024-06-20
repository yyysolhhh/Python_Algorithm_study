h, w = map(int, input().split())
board = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d:
        for i in range(x, x + l):
            board[i][y] = 1
    else:
        for i in range(y, y + l):
            board[x][i] = 1
for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(board[i][j], end=" ")
    print()
