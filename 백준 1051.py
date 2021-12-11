N, M = map(int, input().split())
rect = []
side = min(N, M)
for _ in range(N):
    rect.append(list(map(int, input())))
ans = False
while not ans:
    if side == 1:
        print(1)
        break
    else:
        for i in range(N-side+1):
            for j in range(M-side+1):
                if rect[i][j] == rect[i][j+side-1] and rect[i][j] == rect[i+side-1][j] and rect[i][j] == rect[i+side-1][j+side-1]:
                    print(side * side)
                    ans = True
                    break
            break
        side -= 1
