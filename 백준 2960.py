N, K = map(int, input().split())
prime = [False, False] + [True for _ in range(2, N+1)]
for i in range(2, N+1):
	if prime[i]:
		for j in range(i+i, N+1, i):
			prime[j] = False
			K -= 1
			if K == 0:
				print(j)
				break
