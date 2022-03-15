# from os import chdir
infix = input()
# operator = ['+', '-', '*', '/']
# 1 틀림
# stack1 = []
# stack2 = []
# stack3 = []
# postfix = []
# check = True
# for i in range(len(infix)):
#     if infix[i].isalpha():
#         stack1.append(infix[i])
#     elif infix[i] in operator:
#         stack2.append(infix[i])
#     else:
#         if infix[i] == "(":
#             stack3.append(infix[i])
#             check = True
#         elif infix[i] == ")":
#             stack3.pop()
#     if not stack3 and check:
#         while stack1:
#             postfix.append(stack1.pop(0))
#         while stack2:
#             postfix.append(stack2.pop())
#         check = False
# 2
# stack = []
# postfix = []
# for i in infix:
#     if i.isalpha():
#         postfix.append(i)
#     elif i == '*' or i == '/':
#         stack.append(i)
#     elif i == '+' or i == '-':
#         while stack:
#             postfix.append(stack.pop(0))
#         stack.append(i)
#     else:
#         # if i == '(':
#         # stack.append(i)

#         if i == ')':
#             while stack:
#                 postfix.append(stack.pop())
# print(''.join(postfix))
# # (A+(B*C))-(D/E)

# 3 맞음 (*,/ 우선순위 고려)
stack = []
postfix = []
for i in infix:
    if i.isalpha():
        postfix.append(i)
    else:
        if i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                postfix.append(stack.pop())
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
while stack:
    postfix.append(stack.pop())
print(''.join(postfix))
