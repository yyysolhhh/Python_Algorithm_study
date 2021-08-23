N, K = input().split()
N = int(N)
K = int(K)
circle = [i for i in range(1, N+1)]
o = K - 1
while circle:
    print(o)
    if o > N:
        o = N - K - 1
    print(o)
    del circle[o]
    N -= 1
    o += K - 1
    print(circle)
