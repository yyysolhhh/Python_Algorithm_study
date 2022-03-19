# N * M 크기의 보드에서 8 * 8 크기씩 잘라서 다시 칠해야 할 칸의 개수가 가장 적은 경우 찾기
# W로 시작하는 경우와 B로 시작하는 경우에 어긋나는 칸의 개수를 모두 구해서 result에 append 하고 그 중에 작은 값을 print 한다.
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
