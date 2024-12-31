# 시간 초과
#N, M = map(int, input().split())
#points = sorted(map(int, input().split()))
#for _ in range(M):
#    start, end = map(int, input().split())
#    i, j = 0, len(points) - 1
#    while start > points[i]:
#        i += 1
#    while end < points[j]:
#        j -= 1
#    print(j - i + 1)

def find_start(points, target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if points[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def find_end(points, target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if points[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start

N, M = map(int, input().split())
points = sorted(map(int, input().split()))
for _ in range(M):
    start, end = map(int, input().split())
    i = find_start(points, start)
    j = find_end(points, end)
    print(j - i)
