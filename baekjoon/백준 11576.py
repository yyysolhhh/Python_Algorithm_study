A, B = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))
decimal = 0
remainder = []
# 십진수로 만들기
for i in range(len(num)):
    decimal += num[i] * A ** (len(num) - i - 1)
# B진수로 만들기
while decimal != 0:
    remainder.append(decimal % B)
    decimal //= B
print(' '.join(map(str, remainder[::-1])))
