w, h, b = map(int, input().split())
res = round((w * h * b) / (8 * 1024 * 1025), 2)
print("%.2f" %res, "MB")
