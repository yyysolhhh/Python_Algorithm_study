N = int(input())
row = 1
col = 1
for i in range(N):
    if row >= col:
        col += 1
    else:
        row += 1
print(row * col)
