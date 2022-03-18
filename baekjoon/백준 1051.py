N, M = map(int, input().split())
rect = []
for _ in range(N):
    rect.append(list(map(int, input())))

# 1 틀림
# side = min(N, M)
# check = False
# while not check:
#     for i in range(N-side+1):
#         for j in range(M-side+1):
#             if rect[i][j] == rect[i][j+side-1] == rect[i+side-1][j] == rect[i+side-1][j+side-1]:
#                 ans = side * side
#                 print(ans)
#                 check = True
#                 break
#         break
#     side -= 1

# 2 맞음
ans = 0
for side in range(1, min(N, M)+1):
    for i in range(N):
        for j in range(M):
            if (i + side <= N) and (j + side <= M) and (rect[i][j] == rect[i][j+side-1] == rect[i+side-1][j] == rect[i+side-1][j+side-1]):
                ans = max(side * side, ans)
print(ans)

# 3 2번에서 side 큰것부터 - 틀림
# ans = 1
# for side in range(min(N, M)+1, 0, -1):
#     for i in range(N):
#         for j in range(M):
#             if (i + side <= N) and (j + side <= M) and (rect[i][j] == rect[i][j+side-1] == rect[i+side-1][j] == rect[i+side-1][j+side-1]):
#                 ans = side * side
#                 break
#         else:
#             break
#     else:
#         break
# print(ans)
