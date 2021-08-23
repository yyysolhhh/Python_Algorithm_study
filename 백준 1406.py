import sys
string = list(sys.stdin.readline().strip())
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
            del string[cursor]
            cursor -= 1
    elif command[0] == "P":
        print(string[cursor])
        string.insert(cursor, command[2])
        cursor += 1
    print(cursor)
    print(string)
print("".join(string))
