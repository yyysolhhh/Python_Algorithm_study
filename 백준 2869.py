import sys
A, B, V = map(int, sys.stdin.readline().split())
day = V//(A-B) - 1
h = (A-B) * day
V -= h
while (h <= V):
    h += A
    day += 1
    if (h >= V):
        break
    else:
        h -= B
print(day)
