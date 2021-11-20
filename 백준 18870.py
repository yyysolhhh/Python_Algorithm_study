N = int(input())
X = list(map(int, input().split()))
Xp = []
for i in range(N):
    temp = 0
    for j in set(X):
        if X[i] > j:
            temp += 1
    Xp.append(temp)

print(*Xp)
