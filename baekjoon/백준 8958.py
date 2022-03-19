N = int(input())
case = []
for _ in range(N):
    score = 0
    combo = 0
    case = list(input())
    for i in case:
        if i == 'O':
            combo += 1
            score += combo
        elif i == 'X':
            combo = 0
    print(score)
