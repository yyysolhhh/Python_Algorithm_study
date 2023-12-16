# 6041
a, b = map(int, input().split())
print(a % b)

# 6042
a = float(input())
print(format(a, ".2f"))

# 6043
f1, f2 = map(float, input().split())
print(format(f1 / f2, ".3f"))

# 6044
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, ".2f"))

# 6045
a, b, c = map(int, input().split())
sum = a + b + c
avg = sum / 3
print(sum, format(avg, ".2f"))

# 6046
a = int(input())
print(a << 1)

# 6047
a, b = map(int, input().split())
print(a << b)

# 6048
a, b = map(int, input().split())
print(True if a < b else False)

# 6049
a, b = map(int, input().split())
print(True if a == b else False)

# 6050
a, b = map(int, input().split())
print(True if b >= a else False)