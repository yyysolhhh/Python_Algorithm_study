M, N = map(int, input().split())
for i in range(M, N+1):
    count_d = 0
    for j in range(1, i+1):
        if i % j == 0:
            count_d += 1
    if count_d == 2:
        print(i)
