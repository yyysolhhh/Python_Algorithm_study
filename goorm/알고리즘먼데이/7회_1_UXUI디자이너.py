# 맞음
N, M = map(int, input().split())
event = [0 for _ in range(N + 1)]
for _ in range(M):
    num = list(map(int, input().split()))
    for i in num[1:]:
        event[i] += 1
max_num = max(event)
for i, num in reversed(list(enumerate(event))):
    if num == max_num:
        print(i, end=' ')
