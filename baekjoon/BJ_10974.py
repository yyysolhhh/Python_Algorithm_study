# 다른 방법 - permutations 사용
from itertools import permutations
N = int(input())
pmt = [i for i in range(1, N+1)]
for i in list(permutations(pmt)):
    print(*i)

# 백준에서 Type Error 나옴
N = int(input())
first_perm = [i for i in range(1, N+1)]
perm = first_perm


def permutation(n, perm):
    for i in range(n-1, 0, -1):
        if perm[i] > perm[i-1]:
            for j in range(n-1, i-1, -1):
                if perm[i-1] < perm[j]:
                    perm[i-1], perm[j] = perm[j], perm[i-1]
                    perm[i:] = sorted(perm[i:])
                    return perm


while True:
    print(*perm)
    perm = permutation(N, perm)
    if perm == sorted(first_perm, reverse=True):
        print(*perm)
        break
