import sys
input = sys.stdin.readline
string = input().strip()
bomb = input().strip()
stack = []

# 시간 초과
# while bomb in string:
#     string = string.replace(bomb, '')

for i in string:
    stack.append(i)
    if (stack[-1] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb):
        del stack[-len(bomb):]
if not len(stack):
    print("FRULA")
else:
    print(''.join(stack))
