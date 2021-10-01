N = int(input())
num = 0
while N:
    N -= (int(N**0.5))**2
    num += 1
print(num)
