N = int(input())
arr = [1, 3, 9]
for i in range(N):
    j = i + 1
    while 3 ** i + 3 ** j < 3 ** (i+2) + 3 ** (i+1):
        arr.append(3 ** i + 3 ** j)
        # print(3 ** i, 3 ** j, 3 ** i + 3 ** j)
        j += 1
print(sorted(arr)[N-1])
