# 시간 초과
# import sys
# string = list(sys.stdin.readline().strip())
# N = len(string)
# M = int(sys.stdin.readline())
# cursor = N
# for _ in range(M):
#     command = sys.stdin.readline()
#     if command[0] == "L":
#         if cursor != 0:
#             cursor -= 1
#     elif command[0] == "D":
#         if cursor != N:
#             cursor += 1
#     elif command[0] == "B":
#         if cursor != 0:
#             del string[cursor-1]
#             cursor -= 1
#     elif command[0] == "P":
#         string.insert(cursor, command[2])
#         cursor += 1
# print("".join(string))

import sys
string = list(sys.stdin.readline().strip())
stack = []
N = len(string)
M = int(sys.stdin.readline())
for _ in range(M):
    command = sys.stdin.readline()
    if command[0] == "L":
        if string:
            stack.append(string.pop())
    elif command[0] == "D":
        if stack:
            string.append(stack.pop())
    elif command[0] == "B":
        if string:
            string.pop()
    elif command[0] == "P":
        string.append(command[2])
        # stack.append(command[2])  # 이건 왜 안되지? -> 커서가 이동을 안함
print("".join(string + list(reversed(stack))))
