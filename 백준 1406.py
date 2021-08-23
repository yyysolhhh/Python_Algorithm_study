import sys
string = list(sys.stdin.readline())
N = len(string)
M = int(sys.stdin.readline())
cursor = N
for _ in range(M):
    command = sys.stdin.readline()
    if command[0] == "L":
        if cursor != 0:
            cursor -= 1
    elif command[0] == "D":
        if cursor != N:
            cursor += 1
    elif command[0] == "B":
        if cursor != 0:
            del string[cursor-1]
            cursor -= 1
    elif command[0] == "P":
        string.insert(cursor-1, command[2])
        cursor += 1
print("".join(string))
