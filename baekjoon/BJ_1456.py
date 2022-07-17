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

# 2 - 1 메모리 초과, 틀림
# A, B = map(int, input().split())
# arr = [False] * 2 + [True for _ in range(2, B+1)]
# primes = []
# almst_prime = []
# for i in range(2, B+1):
#     if arr[i]:
#         primes.append(i)
#         for j in range(i+i, B+1, i):
#             arr[j] = False
# for i in primes:
#     for j in range(2, B):
#         if i ** j > B:
#             break
#         almst_prime.append(i ** j)
# print(len(almst_prime))

# 2 - 1 - 2 메모리 초과, 틀림
# A, B = map(int, input().split())
# arr = [False] * 2 + [True for _ in range(2, B+1)]
# almst_prime = []
# for i in range(2, B+1):
#     if arr[i]:
#         for k in range(2, B):
#             if i ** k > B:
#                 break
#             almst_prime.append(i ** k)
#         for j in range(i+i, B+1, i):
#             arr[j] = False
# print(len(almst_prime))

# 2 - 1 - 3 메모리 초과, 틀림
# A, B = map(int, input().split())
# arr = [False] * 2 + [True for _ in range(2, B+1)]
# primes = []
# almst_prime = []
# cnt = 0
# for i in range(2, B+1):
#     if arr[i]:
#         primes.append(i)
#         for j in range(i+i, B+1, i):
#             arr[j] = False
# for alm in primes:
#     i = alm
#     while True:
#         alm *= i
#         if alm >= B:
#             break
#         else:
#             cnt += 1
# print(cnt)

# 2 - 1 - 4 틀림
# A, B = map(int, input().split())
# rB = int(B**0.5)
# arr = [False] * 2 + [True for _ in range(2, rB+1)]
# cnt = 0
# for i in range(2, rB+1):
#     if arr[i]:
#         k = i
#         while True:
#             i *= k
#             if i >= B:
#                 break
#             else:
#                 cnt += 1
#         for j in range(k+k, rB+1, k):
#             arr[j] = False
# print(cnt)

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
