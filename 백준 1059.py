# from itertools import combinations
import sys
input = sys.stdin.readline
L = int(input())
S = [0] + sorted(map(int, input().split()))
n = int(input())
cnt = 0
if n in S:
    print(0)
else:
    # 1 틀림
    # for i in range(L-1):
    #     if S[i] < n and n < S[i+1]:
    #         min_v = S[i] + 1
    #         max_v = S[i+1]
    #         section = sorted(combinations(range(min_v, max_v), 2))
    #         cnt = len(section)
    #         # print(section, cnt)
    #         for j in section:
    #             # print(j)
    #             if n < j[0] or j[1] < n:
    #                 cnt -= 1
    #                 # print('rmv')
    #         # print(section)
    #         break
    #     else:
    #         continue
    # print(cnt)

    # 2
    if len(S) == 1:
        if n < S[0]:
            min_v = 0
            max_v = S[0] - 1
        else:
            min_v = S[0] + 1
            max_v = 1001
    else:
        for i in range(L-1):
            if S[i] < n or n < S[i+1]:
                min_v = S[i] + 1
                max_v = S[i+1] - 1
                break
    cnt = (n - min_v) * (max_v - n + 1) + (max_v - n)
    print(cnt)
