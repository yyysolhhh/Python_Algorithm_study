D, H, W = map(int, input().split())
x = D / ((H * H + W * W) ** 0.5)
print(int(H * x), int(W * x))
