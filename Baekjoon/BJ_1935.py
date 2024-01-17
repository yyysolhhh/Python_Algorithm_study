def calculate(op):
    if op == "+":
        return stack.pop() + stack.pop()
    elif op == "-":
        return - stack.pop() + stack.pop()
    elif op == "*":
        return stack.pop() * stack.pop()
    elif op == "/":
        return 1/stack.pop() * stack.pop()


N = int(input())  # 피연산자 개수
expression = input()  # 후위표기식
value = [0 for i in range(N)]   # 피연산자에 대응하는 값 리스트
for i in range(N):
    value[i] = int(input())   # 대응 값 입력
stack = []
operation = ['+', '-', '*', '/']

for i in range(len(expression)):
    if expression[i].isalnum():   # 피연산자일 때
        # 대응하는 자연수로 바꿔서 스택에 저장
        stack.append(value[ord(expression[i]) - ord('A')])
    elif expression[i] in operation:    # 연산자일 때
        # 스택에 있는 값 두 개씩 빼서 연산자 별로 계산하고 스택에 저장
        stack.append(calculate(expression[i]))
print('%0.2f' % stack[0])   # 스택에 남아있는 결과값 소수점 두 자리까지 출력
print(format(stack[0], ".2f"))
