import string


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
value = []
for _ in range(N):
    value.append(int(input()))
stack = []
operation = ['+', '-', '*', '/']
operand = [i for i in string.ascii_uppercase]

# for i in range(len(expression)):
#   if expression[i+2] == "+":
#     stack.append(expression[i] + expression[i+1])
for i in range(len(expression)):
    if expression[i] in operand:
        stack.append(value.pop(0))
    elif expression[i] in operation:
        stack.append(calculate(expression[i]))
print(round(stack[-1], 3))


# for i in expression:
#     stack.append(i)
#     if i in operand:
#         i = value[0]
#     print(stack)
#     if i in operation:
#         stack.append(calculate(stack.pop()))
#         print(stack)
# print(stack)
