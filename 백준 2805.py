def binary(H, mid, start, end, N, M, height):
    while True:
        cut = 0
        for i in range(N):
            if height[i] - mid > 0:
                cut += height[i] - mid
        if cut == M:
            return H[mid]
        elif cut > M:
            # H = H[mid:]
            start = mid
            end = len(H) - 1
            mid = int((start + end) / 2)
            # H += int(H / (2 ** j))
            binary(H, mid, start, end, N, M, height)
        else:
            # H = H[:mid+1]
            end = mid
            mid = int((start + end) / 2)
            # H -= int(H / (2 ** j))
            binary(H, mid, start, end, N, M, height)


N, M = map(int, input().split())
height = sorted(map(int, input().split()))
H = [i for i in range(height[-1])]
mid = H[int(len(H) / 2)]
print(binary(H, mid, 0, N, N, M, height))
