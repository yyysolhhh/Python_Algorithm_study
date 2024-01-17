import sys
input = sys.stdin.readline
submit = [0 for _ in range(31)]
for _ in range(28):
    n = int(input())
    submit[n] = 1
for i in range(1, 31):
    if submit[i] == 0:
        print(i)
