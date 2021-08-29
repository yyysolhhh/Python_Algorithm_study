N = int(input())
factorial = 1
for i in range(1, N+1):
    factorial *= i
fac_str = str(factorial)
for j in range(-1, -len(fac_str), -1):
    if int(fac_str[j]) != 0:
        print(-j-1)
        break
