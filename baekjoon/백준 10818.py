import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

# 1
print(min(nums), max(nums))

# # 2
# nums.sort()
# print(nums[0], nums[-1])

# # 3
# for i in nums:
#     if i > nums[i+1]:
