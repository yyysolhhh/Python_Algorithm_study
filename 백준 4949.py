import sys
input = sys.stdin.readline
while True:
    string = input().rstrip()
    result = "yes"
    if string == '.':
        break
    stack = []
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
                break
    print(result)
    # 틀림
    # if i == '(' or i == '[':
    #     stack.append(i)
    # elif i == ')' and stack[-1] == '(':
    #     stack.pop()
    # elif i == ']' and stack[-1] == '[':
    #     stack.pop()
    # if not stack and i == ')' or i == ']':
    #     break
    # stack.pop()
    # if len(stack):
    #     print("no")
    # else:
    #     print("yes")
