N = int(input())
words = list(input() for _ in range(N))
result = 0
for i in words:
    temp = []
    i = list(i)
    while i:
        if i[0] in temp and i[0] != temp[-1]:
            break
        temp.append(i.pop(0))
    if not i:
        result += 1
print(result)
