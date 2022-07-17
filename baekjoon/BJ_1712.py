A, B, C = map(int, input().split())
# income = 0
# cost = 0
# prod = 0
if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)
    # while income <= cost:
    #     prod += 1
    #     cost = A + B * prod
    #     income = C * prod
    #     print(cost, income, prod)
    # print(prod)
