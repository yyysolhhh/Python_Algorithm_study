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
        elif i == ')' and stack[-1] == '(' or i == ']' and stack[-1] == '[':
            stack.pop()
    stack.pop()
    if len(stack):
        print("no")
    else:
        print("yes")
