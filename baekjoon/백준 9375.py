T = int(input())
for _ in range(T):
    clothes = {}
    n = int(input())
    res = 1
    for _ in range(n):
        name, sort = input().split()
        if sort in clothes:
            clothes[sort] += 1
        else:
            clothes[sort] = 1
            clothes[sort] += 1
    for i in clothes.values():
        res *= i
    print(res - 1)
