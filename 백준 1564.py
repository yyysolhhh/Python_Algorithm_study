import sys
input = sys.stdin.readline
N = int(input())
factorial = 1
cnt = 0
for i in range(2, N+1):
    factorial *= i
for i in str(factorial)[::-1]:
    if i != '0':
        break
    cnt += 1
factorial //= 10 ** cnt
print(str(factorial)[-5:])
