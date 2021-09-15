from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
# 시간 초과
# queue = [i for i in range(2, N+1, 2)]
# while len(queue) != 1:
#     queue.pop(0)
#     queue.append(queue.pop(0))
# print(queue[0])

# 2
deq = deque([i for i in range(1, N+1)])
while len(deq) != 1:
    deq.popleft()
    deq.append(deq.popleft())
print(deq[0])
