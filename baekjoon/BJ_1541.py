exp = input()
nums = exp.split('-')
res = sum(map(int, nums.pop(0).split('+')))

for i in nums:
    res -= sum(map(int, i.split('+')))
print(res)
