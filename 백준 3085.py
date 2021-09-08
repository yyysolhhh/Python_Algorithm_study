def checkContinuousPart():
    for


N = int(input())
color = list(list(input()) for _ in range(N))
maxNum = 0
for i in range(N):
    for j in range(N):
        # 옆자리 바꾸기
        color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
        checkContinuousPart()
        # 원위치
        color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
