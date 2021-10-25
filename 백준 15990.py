import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0 for _ in range(n+1)]
    for i in range(n+1):
