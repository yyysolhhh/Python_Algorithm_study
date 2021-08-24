N, K = input().split()
N = int(N)
K = int(K)
circle = [i for i in range(1, N+1)]
o = K - 1
while circle:
    print(o)
    if o > N:
        o = N - K - 1
    if N == 1:
        o = 0
    print(N, o)
    del circle[o]
    N -= 1
    o += K - 1
    print(circle)
