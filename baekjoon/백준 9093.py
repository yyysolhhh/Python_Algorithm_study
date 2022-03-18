# 1
# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     sentence = list(sys.stdin.readline().split())
#     for word in sentence:
#         for i in range(len(word), 0, -1):
#             print(word[i-1], end='')
#         print(" ", end='')

# 2
# T = int(input())
# for i in range(T):
#     string = list(input().split())
#     for j in string:
#         print(j[::-1], end=" ")

# 3 스택 이용
T = int(input())
for _ in range(T):
    string = input()
    string += " "
    stack = []
    for i in string:
        if i != " ":
            stack.append(i)
        else:
            while(len(stack) != 0):
                print(stack.pop(), end='')
            print(" ", end='')
