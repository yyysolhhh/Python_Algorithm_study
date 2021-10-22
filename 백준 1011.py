T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x  # 실제 이동해야할 거리
    rep = 0   # 이동 횟수의 빈도수
    # 1 틀림
    # cnt = 1    # 이동 횟수
    # moved_d = 0   # 이동한 거리
    # sum_rep = 0
    # rep_num = 0
    # while moved_d < distance:
    #     rep_num += 1
    #     moved_d += 1
    #     sum_rep += rep
    #     if sum_rep == moved_d:
    #         cnt += 1
    #     if cnt % 2 == 1 and rep_num == 2:
    #         rep += 1

    #     if rep_num == 2:
    #         rep_num = 0
    #     print(moved_d, cnt, rep)
    # print(cnt)

    # 2
    while distance > rep * (rep + 1):
        rep += 1
    if distance <= rep ** 2:
        print(2 * rep - 1)
    else:
        print(2 * rep)
