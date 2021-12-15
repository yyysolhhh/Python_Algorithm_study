def check_prime(n):
    for i in range(1, int(n**0.5)):
        if n % i == 0:
            return False
    print(n)
    return True


A, B = map(int, input().split())
prime_num = []
cnt = 0
for i in range(1, B):
    if check_prime(i):
        prime_num.append(i ** 2)
print(prime_num)
for i in prime_num:
    if A <= i and i <= B:
        cnt += 1
print(cnt)
