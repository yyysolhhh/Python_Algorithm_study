sticks = [64, 32, 16, 8, 4, 2, 1]
X = int(input())
res = 0
for i in sticks:
    if i <= X:
        res += 1
        X -= i
print(res)
