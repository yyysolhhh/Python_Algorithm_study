infix = input()
operator = ['+', '-', '*', '/']
stack1 = []
stack2 = []
stack3 = []
postfix = []
for i in range(len(infix)):
    if infix[i].isalpha():
        stack1.append(infix[i])
    elif infix[i] in operator:
        stack2.append(infix[i])
    else:
        if infix[i] == "(":
            stack3.append(infix[i])
        elif infix[i] == ")":
            stack3.pop()
    if not stack3:
        while stack1:
            postfix.append(stack1.pop(0))
        while stack2:
            postfix.append(stack2.pop())
    # print(stack1, stack2, stack3)
    # print(postfix)
print(postfix)
