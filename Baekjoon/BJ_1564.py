# import math
import sys
input = sys.stdin.readline
N = int(input())
ans = 1

for i in range(2, N + 1):
    ans *= i
    while str(ans)[-1] == '0':
        ans //= 10
    # if str(ans)[-1] == '0':
    #     ans = int(str(ans).rstrip('0'))
    ans %= 1000000000000
print(str(ans)[-5:])

# 4
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n


# print(str(factorial(N)).rstrip('0')[-5:])

# 2
# factorial = math.factorial(N)
# print(factorial)
# 1
# factorial = 1
# for i in range(2, N+1):
#     factorial *= i
# 3 시간 초과
# while factorial % 10 == 0:
#     factorial //= 10

# 1 시간 초과
# cnt = 0
# for i in str(factorial)[::-1]:
#     if i != '0':
#         break
#     cnt += 1
# factorial //= 10 ** cnt

# 2 시간 초과
# while factorial % 10 == 0:
#     factorial //= 10
# print(str(factorial)[-5:])

# factorial %= 100000
# print(factorial)
