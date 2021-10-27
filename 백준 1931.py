N = int(input())
info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append([start, end])

# 1 시간 초과, 틀림
# res = 0
# info.sort(key=lambda x: (x[0], x[1]))
# for i in range(N):
#     cnt = 1
#     pre = info[i][1]
#     for j in range(i+1, N):
#         if pre <= info[j][0]:
#             pre = info[j][1]
#             cnt += 1
#     res = max(res, cnt)
# print(res)

# 2   빨리 시작하는 순서가 아니라 빨리 끝나는 순서대로 정렬 (빨리 끝날수록 다음 회의가 많아지기 때문)
info.sort(key=lambda x: (x[1], x[0]))
pre = 0
cnt = 0
for i in range(N):
    if info[i][0] >= pre:
        pre = info[i][1]
        cnt += 1
print(cnt)
