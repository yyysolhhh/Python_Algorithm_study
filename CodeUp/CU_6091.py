a, b, c = map(int, input().split())
d = 1
while d % a or d % b or d % c:
    d += 1
print(d)
