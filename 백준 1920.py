import sys
input = sys.stdin.readline
N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
for i in nums:
    if i in A:
        print(1)
    else:
        print(0)
# 이분탐색
