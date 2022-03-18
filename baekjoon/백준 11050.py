N, K = map(int, input().split())
result = 1
for i in range(N, N-K, -1):
    result *= i
for i in range(K, 0, -1):
    result /= i
print(int(result))
