def to_abs(x, y):
    if x - y >= 0:
        return x - y
    else:
        return y - x


def is_duplicated(board, col):
    for i in range(col):
        if board[i] == board[col]:
            return 1
        if to_abs(board[i], board[col]) == to_abs(i, col):
            return 1
    return 0


def solve(board, col, cnt):
    row = 0
    print(col)
    if col == N:
        cnt += 1
        return
    while row < N:
        board[col] = row
        print(board, cnt, col, row)
        if (is_duplicated(board, col) == 0):
            solve(board, col + 1, cnt)
        row += 1


N = int(input())
board = [0 for _ in range(N)]
cnt = 0

solve(board, 0, cnt)
print(cnt)
