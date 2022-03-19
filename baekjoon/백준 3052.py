import sys
num = []
for i in range(10):
    num.append(int(sys.stdin.readline()))
num = set([i % 42 for i in num])
print(len(num))
