N = int(input())
score = [(i, list(map(int, input().split()))) for i in range(1, N + 1)]
score.sort(key=lambda x: (-x[1][0], x[1][1], x[1][2]))
print(score[0][0])
