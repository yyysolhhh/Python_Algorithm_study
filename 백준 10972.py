N = int(input())
perm = list(map(int, input().split()))
last = True
for i in range(N-1, 0, -1):
    if perm[i] > perm[i-1]:
        for j in range(i, N):
            if perm[i-1] < perm[j]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm[i:].sort()
                break
        print(*perm)
        last = False
        break
if last:
    print(-1)
