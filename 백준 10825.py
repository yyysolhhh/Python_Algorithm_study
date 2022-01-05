import sys
input = sys.stdin.readline
N = int(input())
stds = []

# 1 맞음 - 468ms
# for i in range(N):
#     stds.append(list(input().rstrip().split()))
#     stds[i][1:] = map(int, stds[i][1:])   // 걸리는 시간 아래 방식이랑 똑같음
# stds.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# for i in stds:
#     print(i[0])

# 2 맞음 - 484ms
for i in range(N):
    stds.append(list(input().split()))
stds.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in stds:
    sys.stdout.write(i[0] + '\n')
