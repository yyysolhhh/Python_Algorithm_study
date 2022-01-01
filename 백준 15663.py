# 1 다시 하기
# def series():
#     if len(combi) == M:
#         print(' '.join(map(str, combi)))
#         return
#     for i in num:
#         # if i in combi:
#         #     continue
#         combi.append(i)
#         series()
#         combi.pop()


# N, M = map(int, input().split())
# num = sorted(map(int, input().split()))
# combi = []
# series()

# 2
from itertools import permutations
N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
perms = sorted(set(permutations(nums, M)))
for i in perms:
    print(*i)
