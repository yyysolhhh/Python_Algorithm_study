N = int(input())
ans = []
for _ in range(N):
    nums = list(map(int, input().split()))
    l = len(set(nums))
    if l == 1:
        ans.append(10000 + nums[0] * 1000)
    elif l == 2:
        for i in nums:
            if nums.count(i) == 2:
                n = i
                break
        ans.append(1000 + n * 100)
    else:
        ans.append(max(nums) * 100)
print(max(ans))
