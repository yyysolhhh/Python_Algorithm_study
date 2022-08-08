M, N, H = map(int, input().split())
box = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        box[i].append(list(map(int, input().split())))
print(box)
