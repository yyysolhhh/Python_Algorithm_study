N, nK = map(int, input().split())
K = list(input().split())

#1 시간초과
for i in range(N, 9, -1):
    flag = True
    for j in str(i):
        if int(j) not in K:
            flag = False
            break
    if flag:
        print(i)
        break

#2
for i in range(N, 0, -1):
    if all(j in K for j in str(i)):
        print(i)
        break

#3
from itertools import product

max_len = len(str(N))
while True:
    temp = sorted(product(K, repeat=max_len), reverse=True)
    result = []
    for i in temp:
        ans = int("".join(i))
        if ans <= N:
            result.append(ans)
    if len(result) > 0:
        print(max(result))
        break
    max_len -= 1
