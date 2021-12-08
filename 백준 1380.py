while True:
    n = int(input())
    if n == 0:
        break
    name = []
    for _ in range(n):
        name.append(input())
    for _ in range(2*n-1):
        num, mark = input().split()
