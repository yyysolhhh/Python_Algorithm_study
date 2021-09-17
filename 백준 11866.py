N, K = map(int, input().split())
circle = [i for i in range(1, N+1)]
josephus = []
order = K - 1
while circle:
    if order >= len(circle):
        order -= len(circle)
    else:
        josephus.append(circle.pop(order))
        order += K - 1
print('<' + ', '.join(map(str, josephus)) + '>')
