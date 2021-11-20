import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
Xp = []

# 1 시간 초과
# for i in range(N):
#     temp = 0
#     for j in set(X):
#         if X[i] > j:
#             temp += 1
#     Xp.append(temp)

for i in X:
    Xp.append(sorted(set(X)).index(i))

print(*Xp)
