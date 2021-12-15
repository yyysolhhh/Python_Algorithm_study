# 1 틀림
# def check_prime(n):
#     for i in range(2, int(n ** 0.5)):
#         if n % i == 0:
#             return False
#     print(n)
#     return True


# A, B = map(int, input().split())
# almst_prime = []
# cnt = 0
# for i in range(2, int(B ** 0.5)+1):
#     if check_prime(i):
#         for j in range(2, B):
#             if i ** j > B:
#                 break
#             almst_prime.append(i ** j)
# print(set(almst_prime))
# for i in set(almst_prime):
#     if A <= i and i <= B:
#         cnt += 1
# print(cnt)

# 2 - 1 메모리 초과
A, B = map(int, input().split())
arr = [False] * 2 + [True for _ in range(2, B+1)]
primes = []
almst_prime = []
for i in range(2, B+1):
    if arr[i]:
        primes.append(i)
        for j in range(i+i, B+1, i):
            arr[j] = False
for i in primes:
    for j in range(2, B):
        if i ** j > B:
            break
        almst_prime.append(i ** j)
print(len(set(almst_prime)))

# 2 - 1 - 2
A, B = map(int, input().split())
arr = [False] * 2 + [True for _ in range(2, B+1)]
primes = []
almst_prime = []
for i in range(2, B+1):
    if arr[i]:
        primes.append(i)
        for j in range(i+i, B+1, i):
            arr[j] = False
for i in primes:
    for j in range(2, B):
        if i ** j > B:
            break
        almst_prime.append(i ** j)
print(len(set(almst_prime)))

# 2 - 2
# A, B = map(int, input().split())
# arr = [False] * 2 + [True for _ in range(2, B+1)]
# primes = []
# for i in range(2, int(B**0.5)+1):
#     if arr[i]:
#         for j in range(i+i, B+1, i):
#             arr[j] = False
# for i in range(len(arr)):
#     if arr[i]:
#         primes.append(i)
# print(primes)
