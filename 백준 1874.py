n = int(input())
stack = []
operation = []
for i in range(n):
    num = int(input())
    for j in range(1, num+1):
        operation.append("+")
        stack.append(j)

# for i in range(1, n+1):
#     for j in num:
#         if i != j:
#             stack.append(i)
#             print("+")
#         elif i == j:
#             stack.pop()
#             print("-")
