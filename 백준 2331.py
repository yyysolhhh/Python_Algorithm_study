# 1 맞음
# A, P = input().split()
# P = int(P)
# D = [int(A)]
# while True:
#     temp = 0
#     for i in str(D[-1]):
#         temp += int(i) ** P
#     if temp in D:
#         D = D[:D.index(temp)]
#         break
#     else:
#         D.append(temp)
# print(len(D))

# 2
A, P = input().split()
P = int(P)
D = [int(A)]
while True:
    temp = 0
    for i in str(D[-1]):
        temp += int(i) ** P
    if temp in D:
        print(D.index(temp))
        break
    else:
        D.append(temp)
