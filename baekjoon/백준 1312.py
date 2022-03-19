A, B, N = map(int, input().split())

# 1 틀림
# temp = str(A / B)
# if len(temp) > N + 1:
#     print(temp[N+1])
# else:
#     print(0)

# 2 맞음
A %= B
for _ in range(N-1):
    A = (A * 10) % B
print(A * 10 // B)
