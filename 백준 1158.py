N, K = input().split()
N = int(N)
K = int(K)
circle = [i for i in range(1, N+1)]
josephus = []
order = K - 1
while circle:
    if order > N:
        order = N - K - 1
    if N == 1:
        order = 0
    josephus.append(str(circle.pop(order)))
    N -= 1
    order += K - 1
print("<" + ", ".join(josephus) + ">")
