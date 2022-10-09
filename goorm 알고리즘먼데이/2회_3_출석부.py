N, k = map(int, input().split())
lst = []
for _ in range(N):
    S, t = input().split()
    lst.append((S, float(t)))
lst.sort(key=lambda x: (x[0], x[1]))
print(lst[k - 1][0], "{:.2f}".format(lst[k - 1][1]))
