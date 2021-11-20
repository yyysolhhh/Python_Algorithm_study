import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
Xs = sorted(set(X))
# Xp = {}

# 1 시간 초과
# for i in range(N):
#     temp = 0
#     for j in set(X):
#         if X[i] > j:
#             temp += 1
#     Xp.append(temp)

# 2 시간 초과
# for i in X:
#     Xp.append(sorted(set(X)).index(i))

# 3
Xp = {Xs[i]: i for i in range(len(Xs))}
for i in X:
    print(Xp[i], end=' ')
