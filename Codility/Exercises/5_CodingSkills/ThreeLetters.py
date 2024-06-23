# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 6%
def solution(A, B):
    if A <= 2 and B <= 2:
        return 'a' * A + 'b' * B
    if A >= B:
        res = ['a' for _ in range(A + B)]
        i = 2
        while B:
            if i >= A + B:
                i = 0
            res[i] = 'b'
            B -= 1
            i += 3
    else:
        res = ['b' for _ in range(A + B)]
        i = 2
        while A:
            if i >= A + B:
                i = 0
            res[i] = 'a'
            A -= 1
            i += 3
    return "".join(res)

# 6%
from itertools import permutations, groupby

def solution(A, B):
    letters = ['a'] * A + ['b'] * B
    perm_list = permutations(letters, A + B)
    for p in perm_list:
        max_len = max(list(len(list(g)) for k, g in groupby(p)))
        if max_len < 3:
            return "".join(p)

