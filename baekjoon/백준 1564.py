import math
import sys
input = sys.stdin.readline
N = int(input())

# 2
factorial = math.factorial(N)
print(factorial)
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
while factorial % 10 == 0:
    factorial //= 10
print(str(factorial)[-5:])

# factorial %= 100000
# print(factorial)
