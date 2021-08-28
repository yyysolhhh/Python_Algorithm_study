# 시간 초과
# import sys
# M, N = map(int, sys.stdin.readline().split())
# for i in range(M, N+1):
#     count_d = 0   # 약수 개수
#     for j in range(1, i+1):
#         if i % j == 0:
#             count_d += 1    # M, N 사이의 수 i를 1, i 사이의 수 j로 나눈 나머지가 0일 때 약수 개수 +1
#     if count_d == 2:
#         print(i)    # 약수 개수가 2일 때 소수 출력

import sys
M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime = False
            continue
    if prime == True:
        print(i)
