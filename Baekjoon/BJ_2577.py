A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)
# 1
num = [0 for i in range(10)]
for i in mul:
    if i == '0':
        num[0] += 1
    elif i == '1':
        num[1] += 1
    elif i == '2':
        num[2] += 1
    elif i == '3':
        num[3] += 1
    elif i == '4':
        num[4] += 1
    elif i == '5':
        num[5] += 1
    elif i == '6':
        num[6] += 1
    elif i == '7':
        num[7] += 1
    elif i == '8':
        num[8] += 1
    elif i == '9':
        num[9] += 1
for i in num:
    print(i)
# # 2
# for i in range(num):
#     print(num.count(str(i)))
