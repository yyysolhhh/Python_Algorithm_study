N, M = map(int, input().split())
board = list(input() for _ in range(M))
for i in range(N-8):
    for j in range(M-8):
        for a in range(i, i+8):
            for b in range(j, j+8):

                # wb = 0
                # bw = 0
                # # for i in range(0, M, 2):
                # #     for j in range(0, N-1, 2):
                # #         if board[i][j:j+2] != 'WB' and [row[j] for row in board[i:i+2]] != ['W', 'B'] or board[i+1][j:j+2] != 'BW' and [row[j+1] for row in board[i:i+2]] != ['B', 'W']:
                # #             wb += 1
                # #         if board[i][j:j+2] != 'BW' and [row[j] for row in board[i:i+2]] != ['B', 'W'] or board[i+1][j:j+2] != 'WB' and [row[j+1] for row in board[i:i+2]] != ['W', 'B']:
                # #             bw += 1
                # #         print(board[i][j:j+2], i, j)
                # #         print(board[i+1][j:j+2], i+1, j)
                # for i in range(0, M, 2):
                #     for j in range(0, N-1, 2):
                #         if board[i][j:j+2] != 'WB' or board[i+1][j:j+2] != 'BW':
                #             wb += 1
                #         if board[i][j:j+2] != 'BW' or board[i+1][j:j+2] != 'WB':
                #             bw += 1
                #         print(board[i][j:j+2], i, j)
                #         print(board[i+1][j:j+2], i+1, j)
                # for i in range(0, M-1, 2):
                #     for j in range(0, N, 2):
                #         if [row[j] for row in board[i:i+2]] != ['W', 'B'] or [row[j+1] for row in board[i:i+2]] != ['B', 'W']:
                #             wb += 1
                #         if [row[j] for row in board[i:i+2]] != ['B', 'W'] or [row[j+1] for row in board[i:i+2]] != ['W', 'B']:
                #             bw += 1
                #         print([row[j] for row in board[i:i+2]], i, j)
                #         print([row[j+1] for row in board[i:i+2]], i, j+1)
                # result = min(wb, bw)
                # print(result)

                # wrong = []
                # for i in range(N):
                #     for j in range(M-1):
                #         if board[i][j] == board[i][j+1]:
                #             wrong.append(board[i][j])
                # b = wrong.count('B') / 2
                # w = wrong.count('W') / 2
                # print(min(b, w))
