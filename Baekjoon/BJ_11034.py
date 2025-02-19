#1
while True:
    try:
        A, B, C = map(int, input().split())
        ans = max(C - B, B - A) - 1
        print(ans)
    except EOFError:
        break

#2
import sys
lines = sys.stdin.readlines()
for line in lines:
    A, B, C = map(int, line.split())
    ans = max(C - B, B - A) - 1
    print(ans)
