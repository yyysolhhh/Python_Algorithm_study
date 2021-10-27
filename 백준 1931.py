N = int(input())
info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append([start, end])
info.sort(key=lambda x: (x[0], x[1]))
res = 0
print(info)
for i in range(N):
    cnt = 1
    pre = info[i][1]
    for j in range(i+1, N):
        print(info[i], info[j], cnt)
        if pre <= info[j][0]:
            pre = info[j][1]
            cnt += 1
            print('!')
    res = max(res, cnt)
print(res)
