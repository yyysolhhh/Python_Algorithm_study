N, K = map(int, input().split())
prime = [False, False] + [True for _ in range(2, N+1)]
for i in range(2, N+1):
    if prime[i]:
        for j in range(i, N+1, i):
            if prime[j]:
                prime[j] = False
                K -= 1
                # print(j, K)
                if K == 0:
                    print(j)
                    break
