import sys
input = sys.stdin.readline
N = int(input())
factorial = 1
last = True
cnt = 0
res = ''
for i in range(2, N+1):
    factorial *= i
for i in str(factorial)[::-1]:
    if i != '0':
        last = False
    if i != '0':
        res += i
        cnt += 1
    if cnt == 5:
        break
print(res[::-1])
