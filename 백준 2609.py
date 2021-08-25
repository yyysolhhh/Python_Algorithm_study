n, m = map(int, input().split())
nd, md = [], []
cd = 0
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
            cd = j
# 최소공배수
cm = int((n/cd) * (m/cd) * cd)
print(cd, cm)
