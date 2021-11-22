from itertools import combinations
L = int(input())
S = sorted(map(int, input().split()))
n = int(input())
cnt = 0
if n in S:
    print(0)
else:
    # 1 틀림
    # for i in range(L-1):
    #     if S[i] < n and n < S[i+1]:
    #         min = S[i] + 1
    #         max = S[i+1]
    #         section = sorted(combinations(range(min, max), 2))
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
    for i in range(L-1):
        if S[i] < n and n < S[i+1]:
            min = S[i] + 1
            max = S[i+1] - 1
            break
        else:
            continue
    cnt = (n - min) * (max - n + 1) + (max - n)
    print(cnt)
