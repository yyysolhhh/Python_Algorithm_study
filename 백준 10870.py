# 1
# n = int(input())
# f = [0 for i in range(n+1)]
# f[0] = 0
# f[1] = 1
# for i in range(2, n+1):
#     f[i] = f[i-2] + f[i-1]
# print(f[n])

# 2
# n = int(input())
# f = [0, 1]
# for i in range(2, n+1):
#     sum = f[i-2] + f[i-1]
#     f.append(sum)
# print(f(n))

# 3
def fibonacci(n):
    return fibonacci(n-2) + fibonacci(n-1)


n = int(input())
print(fibonacci(n))
