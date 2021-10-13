# 2 mid +- 1 왜 하는 건지 아직 모르겠음
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
# height = sorted(map(int, input().split()))
height = list(map(int, input().split()))
start = 0
# end = height[-1]
end = max(height)
while start <= end:
    # mid = int((start + end) / 2)
    mid = (start + end) // 2
    cut = 0
    # print(start, end, mid)
    for i in height:
        if i - mid > 0:
            cut += i - mid
    if cut < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)


# 1 시간 초과 다시하자
# def binary(H, mid, start, end, N, M, height):
#     while True:
#         cut = 0
#         for i in range(N):
#             if height[i] - mid > 0:
#                 cut += height[i] - mid
#         if cut == M:
#             return H[mid]
#         elif cut > M:
#             # H = H[mid:]
#             start = mid
#             end = len(H) - 1
#             mid = int((start + end) / 2)
#             # H += int(H / (2 ** j))
#             binary(H, mid, start, end, N, M, height)
#         else:
#             # H = H[:mid+1]
#             end = mid
#             mid = int((start + end) / 2)
#             # H -= int(H / (2 ** j))
#             binary(H, mid, start, end, N, M, height)


# N, M = map(int, input().split())
# height = sorted(map(int, input().split()))
# H = [i for i in range(height[-1])]
# mid = H[int(len(H) / 2)]
# print(binary(H, mid, 0, N, N, M, height))
