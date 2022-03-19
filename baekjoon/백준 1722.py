from itertools import permutations
N = int(input())
Q = list(map(int, input().split()))
s_num = Q.pop(0)
perm = list(permutations(range(1, N+1)))
print(perm)
if s_num == 1:
    print(*perm[Q[0]-1])
elif s_num == 2:
    print(perm.index(tuple(Q)) + 1)
