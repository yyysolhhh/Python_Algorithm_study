def check_side(x1, y1, x2, y2):
    side = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return side


T = int(input())
for _ in range(T):
    coord = []
    for _ in range(4):
        coord.append(list(map(int, input().split())))
    coord.sort(key=lambda x: (x[0], x[1]))
    length = []
    for i in range(4):
        for j in range(i+1, 4):
            length.append(check_side(
                coord[i][0], coord[i][1], coord[j][0], coord[j][1]))
    length.sort()
    if length[0] == length[1] == length[2] == length[3] and length[4] == length[5]:
        print(1)
    else:
        print(0)
