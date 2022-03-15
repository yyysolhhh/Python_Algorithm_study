N, K = map(int, input().split())
circle = [i for i in range(1, N+1)]
order = K - 1
while len(circle) != 1:
    if order >= len(circle):
        order -= len(circle)
    else:
        circle.pop(order)
        order += K - 1
print(circle[0])
