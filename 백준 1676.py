N = int(input())
factorial = 1
for i in range(1, N+1):
    factorial *= i
fac_str = list(reversed(str(factorial)))
for j in range(len(fac_str)):
    if int(fac_str[j]) != 0:
        print(j)
        break
