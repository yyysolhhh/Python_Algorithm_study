import sys
import heapq
input = sys.stdin.readline
N = int(input())

# 1 시간초과
# arr = []
# for _ in range(N):
#     x = int(input())
#     if x > 0:
#         arr.append(x)
#     elif x == 0:
#         if arr:
#             print(max(arr))
#             arr.remove(max(arr))
#         else:
#             print(0)

# 2 heapq 모듈 사용
heap = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, (-x, x))
    elif x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
