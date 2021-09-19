N, M = map(int, input().split())
board = list(input() for _ in range(N))
result = []
for i in range(N-7):
    for j in range(M-7):
        wb = 0
        bw = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        wb += 1
                    if board[a][b] != 'B':
                        bw += 1
                else:
                    if board[a][b] != 'B':
                        wb += 1
                    if board[a][b] != 'W':
                        bw += 1
        result.append(wb)
        result.append(bw)
print(min(result))
