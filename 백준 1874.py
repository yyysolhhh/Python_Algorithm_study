n = int(input())
num = []
stack = []
for _ in range(n):
    num.append(int(input()))
for i in range(1, n+1):
    for j in num:
        if i != j:
            stack.append(i)
            print("+")
        elif i == j:
            stack.pop()
            print("-")
