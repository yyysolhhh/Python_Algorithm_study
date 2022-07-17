def gcd(A, B):
    while B:
        A, B = B, A % B
    return A * '1'


A, B = map(int, input().split())
print(gcd(A, B))

# for i in range(1, 30):
#     for j in range(1, 30):
#         c = int('1' * i)
#         d = int('1' * j)
#         print(i, j, len(str(gcd(c, d))))
