def calculate(op):
    if op == "+":
        return stack.pop() + stack.pop()
    elif op == "-":
        return - stack.pop() + stack.pop()
    elif op == "*":
        return stack.pop() * stack.pop()
    elif op == "/":
        return 1/stack.pop() * stack.pop()


N = int(input())
expression = input()
value = [0 for i in range(N)]
for i in range(N):
    value[i] = int(input())
print(value)
stack = []
operation = ['+', '-', '*', '/']

for i in range(len(expression)):
    if expression[i].isalnum():
        stack.append(value[ord(expression[i]) - ord('A')])
    elif expression[i] in operation:
        stack.append(calculate(expression[i]))
print('%0.2f' % stack[0])
print(format(stack[0], ".2f"))
