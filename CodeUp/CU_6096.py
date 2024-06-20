board = []
for i in range(19):
    board.append(list(map(int, input().split())))
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(19):
        if i != y:
            board[x][i] = 0 if board[x][i] else 1
    for i in range(19):
        if i != x:
            board[i][y] = 0 if board[i][y] else 1
for i in range(19):
    for j in range(19):
        print(board[i][j], end=" ")
    print()
