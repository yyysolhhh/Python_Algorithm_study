X, Y = map(int, input().split())
revX = int(str(X)[::-1])
revY = int(str(Y)[::-1])
print(int(str(revX + revY)[::-1]))
