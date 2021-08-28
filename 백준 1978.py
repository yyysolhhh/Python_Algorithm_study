N = int(input())
num = list(map(int, input().split()))
prime_num = 0
for i in num:
    count_d = 0
    for j in range(1, i+1):
        if i % j == 0:
            count_d += 1
    if count_d == 2:
        prime_num += 1
print(prime_num)
