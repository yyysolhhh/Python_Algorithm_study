X = input()
for i in range(int(X) + 1, 1000000):
    ans = True
    nums = [0 for _ in range(10)]
    for j in str(X):
        nums[int(j)] += 1
    for j in str(i):
        if nums[int(j)] == 0:
            ans = False
            break
        nums[int(j)] -= 1
    if ans:
        print(i)
        break
else:
    print(0)
