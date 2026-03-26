import sys
input = sys.stdin.readline

# 1
N, M = map(int, input().split())
K = list(map(int, input().split()))
nums = set()
for i in K:
    for j in range(N + 1):
        if j % i == 0:
            nums.add(j)
print(sum(nums))

# 2
N, M = map(int, input().split())
K = list(map(int, input().split()))
nums = set()
for i in K:
    for j in range(i, N + 1, i):
        nums.add(j)
print(sum(nums))
