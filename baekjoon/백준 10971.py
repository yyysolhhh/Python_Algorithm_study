from itertools import permutations
import sys
input = sys.stdin.readline

# 1 틀림
# N = int(input())
# W = []
# for _ in range(N):
#     W.append(list(map(int, input().split())))
# paths = list(permutations(range(N)))
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
# N = int(input())
# W = []
# cost = 0
# for _ in range(N):
#     W.append(list(map(int, input().split())))

# 1-2 맞음 (python으로 시간초과)
N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))
paths = permutations(range(N))
cost = sys.maxsize
for p in paths:
    if W[p[-1]][p[0]] != 0:
        temp = 0
        check = True
        for i in range(N-1):
            if W[p[i]][p[i+1]] == 0:
                check = False
                break
            temp += W[p[i]][p[i+1]]
            if temp >= cost:
                check = False
                break
        if check == False:
            continue
        temp += W[p[-1]][p[0]]
        cost = min(cost, temp)
print(cost)

# 1-3 맞음


def main():
    N = int(input())
    W = []
    for i in range(N):
        W.append(list(map(int, input().split())))
    paths = permutations(range(N))
    cost = sys.maxsize
    for p in paths:
        if W[p[-1]][p[0]] == 0:
            continue
        temp = 0
        check = True
        for i in range(N-1):
            start = p[i]
            end = p[i+1]
            if W[start][end] == 0:
                check = False
                break
            temp += W[start][end]
            if temp >= cost:
                check = False
                break
        if check == False:
            continue
        temp += W[p[-1]][p[0]]
        cost = min(cost, temp)
    return cost


print(main())
