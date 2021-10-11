N = int(input())
perm = [i for i in range(1, N+1)]
for i in range(N-1, 0, -1):
    print(*perm)
    if perm[i] > perm[i-1]:
        for j in range(N-1, i-1, -1):
            if perm[i-1] < perm[j]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm[i:] = sorted(perm[i:])
                break
