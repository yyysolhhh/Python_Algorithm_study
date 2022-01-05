N = int(input())
stds = []
for i in range(N):
    stds.append(list(input().split()))
    stds[i][1:] = map(int, stds[i][1:])
stds.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in stds:
    print(i[0])
