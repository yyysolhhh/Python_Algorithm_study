P, K = map(int, input().split())
isPrime = [False, False] + [True for _ in range(2, K)]
isBad = False
for i in range(2, K):
    if isPrime[i]:
        for j in range(i * 2, K, i):
            isPrime[j] = False
for r in range(K):
    if isPrime[r]:
        if P % r == 0:
            isBad = True
            break
if isBad:
    print("BAD", r)
else:
    print("GOOD")
