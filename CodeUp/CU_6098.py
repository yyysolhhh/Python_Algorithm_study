board = []
for _ in range(10):
    board.append(list(map(int, input().split())))
x, y = 1, 1
d = 0
while True:
    if x == 8 and y == 8:
        board[x][y] = 9
        break
    else:
        if board[x][y] == 1:
            if d:
                x -= 1
                d = 0
            else:
                y -= 1
                d = 1
        elif board[x][y] == 2:
            board[x][y] = 9
            break
        else:
            board[x][y] = 9
            if d and board[x][y + 1] == 1:
                x += 1
            else:
                y += 1
for i in range(10):
    for j in range(10):
        print(board[i][j], end=" ")
    print()
