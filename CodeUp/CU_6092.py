n = int(input())
num = list(map(int, input().split()))
d = [0 for _ in range(24)]
for i in num:
    d[i] += 1
for i in d[1:]:
    print(i, end=' ')
