# 1
octal = list(map(int, input()))
binary = []
for i in octal:
    remainder = []
    while i != 0:
        remainder.append(i % 2)
        i //= 2
    while len(remainder) != 3:
        remainder.append(0)
    binary.append(''.join(map(str, remainder[::-1])))
if octal == [0]:
    print(0)
else:
    print(''.join(map(str, binary)).lstrip('0'))

# 2
print(bin(int(input(), 8))[2:])
