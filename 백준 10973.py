N = int(input())
perm = list(map(int, input().split()))
first = True
for i in range(N-1, 0, -1):
    if perm[i] < perm[i-1]:
        for j in range(N-1, i-1, -1):
            if perm[i-1] > perm[j]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm[i:] = sorted(perm[i:], reverse=True)
                break
        print(*perm)
        first = False
        break
if first:
    print(-1)
