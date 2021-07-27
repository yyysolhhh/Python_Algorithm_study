n, m = map(int, input().split())
nd, nm, md, mm, cd, cm = [], [], [], [], [], []
for i in range(1, n+1):
    if n % i == 0:
        nd.append(i)

for i in range(1, m+1):
    if m % i == 0:
        md.append(i)
for i in nd:
    for j in md:
        if i == j:
            cd.append(j)

print(cd[-1])
