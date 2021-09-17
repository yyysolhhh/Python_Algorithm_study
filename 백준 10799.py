# 시간 초과
# import sys
# bra = sys.stdin.readline().strip()
# stick = []
# open = []
# for i in range(len(bra)):
#     if bra[i:i+2] == '((':
#         stick.append(1)
#         open.append(True)
#         # print('((', stick, open)
#     elif bra[i:i+2] == '()':
#         for j in range(len(stick)):
#             if open[j]:
#                 stick[j] += 1
#         # print('()', stick, open)
#     elif bra[i:i+2] == '))':
#         for j in range(len(open)-1, -1, -1):
#             if open[j]:
#                 open[j] = False
#                 break
#         # print('))', stick, open)
# print(sum(stick))

# 시간 초과
# import sys
# bra = sys.stdin.readline().strip()
# stick = []
# result = 0
# for i in range(len(bra)):
#     if bra[i:i+2] == '((':
#         stick.append(1)
#     elif bra[i:i+2] == '()':
#         stick += [1]*len(stick)
#     elif bra[i:i+2] == '))':
#         result += stick.pop()
# print(result)

import sys
bra = sys.stdin.readline().strip()
stick = []
result = 0
for i in range(len(bra)):
    # 1
    # if bra[i] == '(':
    #     stick.append(1)
    #     result += 1
    # else:
    #     if bra[i-1] == '(':
    #         stick.pop()
    #         result += len(stick) - 1
    #     else:
    #         stick.pop()
    # 2
    if bra[i] == '(':
        stick.append(1)
    else:
        if bra[i-1] == '(':
            stick.pop()
            result += len(stick)
        else:
            stick.pop()
            result += 1
print(result)
