N, M = map(int, input().split())
castle = []
for _ in range(N):
    castle.append(list(input()))

# 1 틀림
# res = 0
# for i in range(N):
#     if 'X' not in castle[i]:
#         for j in range(M):
#             if 'X' not in castle[:][j]:
#                 castle[i][j] = 'X'
#                 res += 1
#                 print(i, j)
#                 break
#         else:
#             castle[i][0] = 'X'
#             res += 1
#             print(i, j)
# print(res)

# 2 X가 없는 행, 열의 개수 중 더 큰 값을 출력
row = 0
col = 0
for i in range(N):
    if 'X' not in castle[i]:
        row += 1
for j in range(M):
    if 'X' not in (castle[i][j] for i in range(N)):
        col += 1
print(max(row, col))
