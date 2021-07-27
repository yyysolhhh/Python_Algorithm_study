import sys
C = int(input())
score = []
for _ in range(C):
    score = list(map(int, sys.stdin.readline().split()))
    num = 0
    rate = 0
    avg = sum(score[1:]) / score[0]
    for i in score[1:]:
        if i > avg:
            num += 1
    rate = num / score[0] * 100
    print("%.3f%%" % round(rate, 3))
    print(f'{rate:.3f}%')
