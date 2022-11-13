for _ in range(5):
    a = 0
    num = input()
    for i in range(0, len(num), 2):
        a += int(num[i])
    for i in range(1, len(num), 2):
        if num[i] == '0':
            continue
        a *= int(num[i])
    print(a % 10)
