binary = list(input())
# 2 -> 8
octal1 = []
if len(binary) % 3 != 0:    # 3자리씩 나눠서 계산해야 하므로 앞부분에 0을 채워서 자릿수를 3의 배수로 만들어준다.
    while len(binary) % 3 != 0:
        binary.insert(0, 0)
for i in range(len(binary)//3):   # 8진수로 바로 변환
    three = 0
    for j in range(3):
        three += 2 ** j * int(binary[(-3*i-1)-j])
    octal.append(str(three))
print("".join(octal[::-1]))

# 2 -> 10 -> 8 (시간초과)
decimal = 0
octal2 = []
for i in range(len(binary), 0, -1):   # 10진수로 변환하고 8진수로 변환
    decimal += int(binary[-i]) * 2 ** (i-1)
quotient = decimal
while quotient != 0:
    octal2.append(str(quotient % 8))
    quotient //= 8
print("".join(octal2[::-1]))
