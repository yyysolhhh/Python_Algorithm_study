def factorial(num):
    fac = 1
    for i in range(1, num+1):
        fac *= i
    return fac


n, m = map(int, input().split())
result = 0
result = int(factorial(n) / (factorial(m) * factorial(n - m)))
rev_result = list(reversed(str(result)))
for i in range(len(rev_result)):
    if rev_result[i] != '0':
        print(i)
        break
