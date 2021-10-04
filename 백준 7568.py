N = int(input())
info = []
result = [1 for i in range(N)]
for _ in range(N):
    info.append(list(map(int, input().split())))
for i in range(len(info)):
    for j in range(len(info)):
        if i != j:
            if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                result[i] += 1
# for i in range(len(result)):
#     result[i] += 1
print(*result)
