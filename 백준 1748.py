import sys

# 시간 초과
# def digit(n):
#     return len(str(n))


# N = int(sys.stdin.readline())
# result = 0
# if N < 10:
#     result = N
# elif N < 100 and N >= 10:
#     result += 9 + (N - 9) * 2
# else:
#     result += 9 + 90 * 2
#     for i in range(100, N+1):
#         result += digit(i)
# print(result)

# 2
N = int(sys.stdin.readline())
result = 0
len_N = len(str(N))
for i in range(1, len_N):
    result += i * 9 * 10 ** (i - 1)
result += (N - 10 ** (len_N-1) + 1) * (len_N)
print(result)
