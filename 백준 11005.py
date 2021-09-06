import sys
N, B = map(int, sys.stdin.readline().split())
remainder = []
while N != 0:
    if N % B >= 10:
        remainder.append(chr(N % B + 55))
    else:
        remainder.append(N % B)
    N //= B
print(''.join(map(str, remainder[::-1])))
