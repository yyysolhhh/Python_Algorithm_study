import sys
N = int(input())
score = list(map(int, sys.stdin.readline().split()))
M = max(score)
score = [i / M * 100 for i in score]
# newSum = sum(score)
for i in score:
    newSum += i
print(newSum / N)
