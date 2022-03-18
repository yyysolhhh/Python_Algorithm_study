def d(n):
    num = str(n)
    sum = 0
    for i in num:
        sum += int(i)
    sum += n
    return sum


num_list = [0 for i in range(10001)]

for i in range(1, 10001):
    num_list.append(d(i))

for i in range(1, 10001):
    if i not in num_list:
        print(i)
