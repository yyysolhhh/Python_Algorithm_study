T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    year = min(M, N)
    x1 = min(M, N)
    y1 = min(M, N)
    while True:
        try:
            x1 += 1
            y1 += 1
            year += 1
            if x1 > M:
                x1 = 1
            if y1 > N:
                y1 = 1
            if x1 == x and y1 == y:
                print(year)
                break
        except:
            print(-1)
