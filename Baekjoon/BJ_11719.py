# 1
while True:
    try:
        print(input())
    except EOFError:
        break

# 2
import sys
lines = sys.stdin.readlines()
print("".join(lines))
