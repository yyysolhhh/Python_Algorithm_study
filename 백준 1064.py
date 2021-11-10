xa, ya, xb, yb, xc, yc = map(int, input().split())
if (xb - xa) * (yc - ya) == (xc - xa) * (yb - ya):
    print(-1.0)
else:
    side1 = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
    side2 = ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5
    side3 = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
    sides = sorted([side1, side2, side3])

    # 1
    # length = []
    # for i in range(3):
    #     for j in range(3):
    #         if i == j:
    #             break
    #         length.append((sides[i] + sides[j]) * 2)
    # print(max(length) - min(length))

    # 2
    max_len = (sides[2] + sides[1]) * 2
    min_len = (sides[1] + sides[0]) * 2
    print(max_len - min_len)
