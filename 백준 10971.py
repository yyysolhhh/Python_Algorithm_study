from itertools import combinations, permutations
import sys
input = sys.stdin.readline
N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))
paths = list(permutations(range(N), N))
cost = 100000000
for p in paths:
    temp = 0
    for j in range(len(p)):
        if j == len(p)-1:
            temp += W[p[j]][p[0]]
        else:
            temp += W[p[j]][p[j+1]]
    cost = min(cost, temp)
print(cost)
