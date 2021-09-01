binary = list(input())
octal = []
if len(binary) % 3 != 0:
    while len(binary) % 3 != 0:
        binary.insert(0, 0)
# decimal = 0
# for i in range(len(binary), 0, -1):   # 10진수로 변환
#     decimal += int(binary[-i]) * 2 ** (i-1)
for i in range(len(binary)//3):   # 8진수로 변환
    three = 0
    for j in range(3):
        three += 2 ** j * int(binary[(-3*i-1)-j])
        # print((-3*i-1)-j, binary[(-3*i-1)-j], three)
    octal.append(str(three))
print("".join(octal[::-1]))
