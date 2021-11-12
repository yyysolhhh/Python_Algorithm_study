N, new_score, P = map(int, input().split())
rank = []
if N:
    rank = list(map(int, input().split()))
    rank.append(new_score)
    rank.sort(reverse=True)
    res = rank.index(new_score) + 1
    if res > P:
        print(-1)
    else:
        # 1 틀림
        # if len(rank) > P and res == P and rank[P-1] == rank[P]:
        #     print(-1)
        # 2 틀림
        # if res == P and rank.count(rank[res]) > 1:
        #     print(-1)
        # 3 맞음
        if N == P and new_score == rank[-1]:
            print(-1)
        else:
            print(res)

    # 다른 방법 - 미완성
    # res = 0
    # for i in range(len(rank)):
    #     if new_score < rank[i]:
    #         rank.insert(i+1, new_score)
    #         res = i-1
    #     elif new_score == rank[i]:
    #         rank.insert(i+1, new_score)
    #         res = i
    #     print(rank)
    # if res > P:
    #     print(-1)
    # else:
    #     print(res)
else:
    print(1)
