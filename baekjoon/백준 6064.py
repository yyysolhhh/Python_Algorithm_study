T = int(input())
# 시간 초과
# for _ in range(T):
#     M, N, x, y = map(int, input().split())
#     year = min(M, N)
#     x1 = min(M, N)
#     y1 = min(M, N)
#     while True:
#         x1 += 1
#         y1 += 1
#         year += 1
#         if x1 > M:
#             x1 = 1
#         if y1 > N:
#             y1 = 1
#         if x1 == x and y1 == y:
#             print(year)
#             break
for _ in range(T):
    result = -1

    M, N, x, y = map(int, input().split())
    while x <= M * N:
        if (x - y) % N == 0:
            result = x
            break
        x += M
    print(result)
