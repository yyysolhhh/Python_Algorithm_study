n, m = map(int, input().split())
nd, md = [], []
gcd = 0
# n 약수
for i in range(1, n+1):
    if n % i == 0:
        nd.append(i)
# m 약수
for i in range(1, m+1):
    if m % i == 0:
        md.append(i)
# n, m 최대공약수
for i in nd:
    for j in md:
        if i == j:
            gcd = j
# 최소공배수
lcm = int((n/cd) * (m/cd) * cd)
print(gcd, lcm)

# 2 다른 방법
a, b = map(int, input().split())


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))
