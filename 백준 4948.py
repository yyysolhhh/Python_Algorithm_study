def is_prime(n):
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    else:
        return True


num = [i for i in range(1, 123456 * 2 + 1)]
prime = []
for i in num:
    prime.append(is_prime(i))

while True:
    n = int(input())
    if n == 0:
        break
    print(prime[n:2*n].count(True))


# 1 시간 초과
# while True:
#     n = int(input())
#     res = 0
#     if n == 0:
#         break
#     for i in range(n+1, 2*n+1):
#         if i == 2:
#             res = 1
#             break
#         else:
#             for j in range(2, int(i**0.5)+1):
#                 if i % j == 0:
#                     break
#             else:
#                 res += 1
#     print(res)
