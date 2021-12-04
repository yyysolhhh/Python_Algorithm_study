# # 1
# from itertools import permutations
# import sys
# input = sys.stdin.readline
# N = int(input())
# W = []
# for _ in range(N):
#     W.append(list(map(int, input().split())))
# paths = list(permutations(range(N), N))
# cost = 100000000
# for p in paths:
#     temp = 0
#     for j in range(len(p)):
#         if j == len(p)-1:
#             temp += W[p[j]][p[0]]
#         else:
#             temp += W[p[j]][p[j+1]]
#     cost = min(cost, temp)
# print(cost)

# 2 비트마스크
N = int(input())
W = []
cost = 0
for _ in range(N):
    W.append(list(map(int, input().split())))
