import sys
N = int(sys.stdin.readline())
remainder = []
while N:
    if N % -2:

        remainder.append(N % -2)
        N //= -2
print(remainder)
