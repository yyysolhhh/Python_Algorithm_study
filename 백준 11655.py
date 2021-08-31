S = input()
ROT = []
for i in S:
    if i.isalpha():
        if (ord(i) > ord('m') and ord(i) <= ord('z')) or (ord(i) > ord("M") and ord(i) <= ord("Z")):
            ROT.append(chr(ord(i) - 13))
        else:
            ROT.append(chr(ord(i) + 13))
    else:
        ROT.append(i)
print("".join(ROT))
for i in ROT:
    print(i, end='')
