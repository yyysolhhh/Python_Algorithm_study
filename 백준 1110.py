cycle = 0
N = int(input())
num = N
while True:
    cycle += 1
    num = num % 10 * 10 + (num // 10 + num % 10) % 10
    if num == N:
        break
    print(num)
print(cycle)
