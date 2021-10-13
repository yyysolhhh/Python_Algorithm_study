def binary(H, N, M, height):
    while True:
        cut = 0
        j = 1
        for i in range(N):
            if height[i] - H > 0:
                cut += height[i] - H
        j += 1
        if cut == M:
            return H
        elif cut > M:
            H += int(height[-1] / (2 ** j))
            binary(H, N, M, height)
        else:
            H -= int(height[-1] / (2 ** j))
            binary(H, N, M, height)


N, M = map(int, input().split())
height = sorted(map(int, input().split()))
H = int(height[-1] / 2)
print(binary(H, N, M, height))
