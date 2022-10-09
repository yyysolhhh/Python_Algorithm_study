t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    avg = sum(v) / n
    a = 0
    for i in v:
        if i >= avg:
            a += 1
    print("{}/{}".format(a, n))
