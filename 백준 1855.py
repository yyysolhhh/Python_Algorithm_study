# 문제 잘못 이해함
# K = int(input())
# string = input()
# encryption = []
# for i in range(len(string)//K):
#     if i % 2 == 0:
#         for j in range(K):
#             encryption.append(string[4*j+i])
#             print(i, j)
#     else:
#         for j in range(K-1, -1, -1):
#             encryption.append(string[4*j+i])
#             print(i, j)
# print(encryption)

K = int(input())
encryption = input()
original = []
for i in range(len(encryption)//K):
    if i % 2 == 0:
        original.append(encryption[i*K:i*K+K])
    else:
        original.append(encryption[i*K+K-1:i*K-1:-1])
for i in range(K):
    for j in range(len(original)):
        print(original[j][i], end='')
