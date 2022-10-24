N, M = map(int, input().split())
res = N
waiting = []
for _ in range(M):
    action, k = input().split()
    k = int(k)
    while waiting and waiting[0] <= res:
        res -= waiting[0]
        waiting.pop(0)
    if action == "deposit":
        res += k
    elif action == "pay":
        if res >= k:
            res -= k
    elif action == "reservation":
        if res < k or waiting:
            waiting.append(k)
        else:
            res -= k
while waiting:
    if waiting[0] <= res:
        res -= waiting[0]
        waiting.pop(0)
    else:
        break
print(res)
