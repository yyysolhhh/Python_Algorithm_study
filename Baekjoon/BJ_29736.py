A, B = map(int, input().split())
K, X = map(int, input().split())
# 1
s, e = 0, 0
if K + X < A or K - X > B:
    print("IMPOSSIBLE")
else:
    if K - X < A < K + X:
        s = A
    elif K - X > A:
        s = K - X
    if K - X < B < K + X:
        e = B
    elif K + X < B:
        e = K + X
    print(e - s + 1)

#2
res = 0
for i in range(K - X, K + X + 1):
    if A <= i <= B:
        res += 1
if res:
    print(res)
else:
    print("IMPOSSIBLE")
