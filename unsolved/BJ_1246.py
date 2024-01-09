import sys

input = sys.stdin.readline
N, M = map(int, input().split())
P = []
for _ in range(M):
    P.append(int(input()))
prices = sorted(P, reverse = True)
profit = 0
for i, p in enumerate(prices, start=1):
    i = min(N, i)
    temp = p * i
    if profit < temp:
        profit = temp
        fixed_p = p
#for i, p in enumerate(prices):
#    i = min(N - 1, i)
#    temp = p * (i + 1)
#    if profit < temp:
#        profit = temp
#        fixed_p = p
#    else:
#        break

#    if profit >= temp:
#       break
#    profit = max(profit, temp)
#    fixed_p = p
print(fixed_p, profit)

# 왜 중간에 멈추면 안되는지 알아내기
