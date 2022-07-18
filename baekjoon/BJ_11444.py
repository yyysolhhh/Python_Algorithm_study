# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return (fibonacci(n - 2) + fibonacci(n - 1)) % 1000000007


# n = int(input())
# print(fibonacci(n))

n = int(input())
f = [[1, 1], [1, 0]]
temp = [[1, 1], [1, 0]]
for _ in range(n - 1):
    temp = [[temp[0][0] * f[0][0] + temp[0][1] * f[1][0], temp[0][0] * f[0][1] + temp[0][1] * f[1][1]],
            [temp[1][0] * f[0][0] + temp[1][1] * f[1][0], temp[1][0] * f[0][1] + temp[1][1] * f[1][1]]]
print(temp[0][1] % 1000000007)
