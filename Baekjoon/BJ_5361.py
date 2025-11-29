t = int(input())
price = [350.34, 230.90, 190.55, 125.30, 180.90]
for _ in range(t):
    num = map(int, input().split())
    ans = sum(i * j for i, j in zip(price, num))
    print(f"${ans:.2f}")
