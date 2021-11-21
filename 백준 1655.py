import sys
input = sys.stdin.readline
N = int(input())
baek = []
for _ in range(N):
    baek.append(int(input()))

# 1 시간 초과
queue = []
for i in range(len(baek)):
    queue.append(baek.pop(0))
    queue.sort()
    if len(queue) % 2 == 0:
        print(queue[len(queue)//2-1])
    else:
        print(queue[len(queue)//2])

# 2
