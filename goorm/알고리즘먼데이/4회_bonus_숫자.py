A, B = map(int, input().split())
if (A == B):
    print(0)
else:
    print(B - A - 1)
for x in range(A + 1, B):
    print(x, end=' ')
