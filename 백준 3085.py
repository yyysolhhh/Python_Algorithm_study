def checkContinuousPart():
    result = 1
    for i in range(N-1):
        candy = 1
        for j in range(N-1):
            if color[i][j] == color[i][j+1]:
                candy += 1
            if candy > result:
                result = candy
    for i in range(N-1):
        candy = 1
        for j in range(N-1):
            if color[i][j] == color[i+1][j]:
                candy += 1
            if candy > result:
                result = candy
    return result


N = int(input())
color = list(list(input()) for _ in range(N))
maxNum = 0
for i in range(N):
    for j in range(N-1):
        # 옆자리 바꾸기
        if color[i][j] != color[i][j+1]:
            color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
            # print(color)
            temp = checkContinuousPart()
            if temp > maxNum:
                maxNum = temp
            # 원위치
            color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
for i in range(N-1):
    for j in range(N):
        # 위아래 바꾸기
        if color[i][j] != color[i+1][j]:
            color[i][j], color[i+1][j] = color[i+1][j], color[i][j]
            # print(color)
            temp = checkContinuousPart()
            if temp > maxNum:
                maxNum = temp
            # 원위치
            color[i][j], color[i+1][j] = color[i+1][j], color[i][j]
print(maxNum)
