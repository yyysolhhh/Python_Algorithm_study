N = int(input())
words = list(input() for _ in range(N))
result = 0
for i in words:
    temp = []
    i = list(i)
    for j in i:
        if j in temp and j != temp[-1]:
            break
        temp.append(i.pop())
    print(i, temp)
    if not i:
        result += 1
print(result)
