T = int(input())
group = [1, 3, 5]
for _ in range(T):
    G, C, E = map(int, input().split())
    print((E - C) * group[G - 1] if E - C > 0 else 0)
