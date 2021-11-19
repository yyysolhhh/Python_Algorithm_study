def gcd(A, B):
    while B:
        A, B = B, A % B
    return A


a, b = map(int, input().split())
A = int('1' * a)
B = int('1' * b)
print(gcd(A, B))
