coords = [list(map(int, input().split())) for _ in range(3)]
x = []
y = []
for co in coords:
    if co[0] in x:
        x.remove(co[0])
    else:
        x.append(co[0])
    if co[1] in y:
        y.remove(co[1])
    else:
        y.append(co[1])
print(' '.join(map(str, x + y)))
