# 1 시간 초과
# import sys
# input = sys.stdin.readline
# A, B = map(int, input().split())
# underprime = 0
# prime_list = [False, False] + [True for _ in range(2, B+1)]
# for i in range(2, int(B**0.5)+1):
#     if prime_list[i]:
#         for j in range(i+i, B+1, i):
#             prime_list[j] = False
# for i in range(A, B+1):
#     prime = 0
#     for j in range(2, i+1):
#         if prime_list[j]:
#             while i % j == 0:
#                 i //= j
#                 prime += 1
#     if prime_list[prime]:
#         underprime += 1
# print(underprime)

# 2
import sys
input = sys.stdin.readline
A, B = map(int, input().split())
underprime = 0
prime_list = [False, False] + [True for _ in range(2, B+1)]
n_factor = [0 for _ in range(B+1)]
for i in range(2, B+1):
    if prime_list[i]:
        for j in range(i+i, B+1, i):
            prime_list[j] = False
            temp = j
            while temp % i == 0:
                temp //= i
                n_factor[j] += 1
for i in range(A, B+1):
    if prime_list[n_factor[i]]:
        underprime += 1
print(underprime)
