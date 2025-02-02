import sys
input = sys.stdin.readline

def binarysearch(n, arr):
    start, end = 0, len(arr) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < n:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(map(int, input().split()))
    ans = 0
    for i in A:
        ans += binarysearch(i, B) + 1
    print(ans)
