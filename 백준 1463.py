import sys
N = int(sys.stdin.readline())
times = 0
while N != 1:
    times += 1
    if N % 3 == 0:
        N /= 3
    if N % 2 == 0:
        N /= 2
    else:
        N -= 1

print(int(N), times)
