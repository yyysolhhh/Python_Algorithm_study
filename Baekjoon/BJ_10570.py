N = int(input())
for _ in range(N):
    V = int(input())
    nums = dict()
    for _ in range(V):
        S = int(input())
        if S not in nums:
            nums[S] = 0
        nums[S] += 1
    nums = sorted(nums.items(), key=lambda x: (-x[1], x[0]))
    print(nums[0][0])
