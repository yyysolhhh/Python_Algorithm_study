n, m = map(int, input().split())
perm = 1
m_fac = 1
for i in range(n, n - m, -1):
    perm *= i
for i in range(2, m + 1):
    m_fac *= i
print(perm // m_fac)
