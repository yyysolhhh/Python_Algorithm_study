import sys
input = sys.stdin.readline
while True:
    string = input().strip()
    if string == '.':
        break
    stack = [0]
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        if not stack and i == ')' or i == ']':
            break
    stack.pop()
    if len(stack):
        print("no")
    else:
        print("yes")
