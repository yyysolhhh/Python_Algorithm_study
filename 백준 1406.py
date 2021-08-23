import sys
N = list(sys.stdin.readline())
M = int(sys.stdin.readline())
cursor = N
for _ in range(M):
    command = sys.stdin.readline()
    if command[0] == "L":
        cursor -= 1

    elif command[0] == "D":
        cursor += 1

    elif command[0] == "B":

    elif command[0] == "P":
