# 1
N, M = map(int, input().split())
streak = dict()
for _ in range(N):
    line = input().split()
    *record, name = line
    max_streak = 0
    temp = 0
    for i in record:
        if i == ".":
            temp += 1
        elif i == "*":
            temp = 0
        max_streak = max(max_streak, temp)
    streak[name] = max_streak
print(len(set(streak.values())))
for name, num in streak.items():
    print(num, name)

# 2
N, M = map(int, input().split())
count = set()
streak = []
for _ in range(N):
    line = input().split()
    record = line[:M]
    name = line[-1]
    max_streak = 0
    temp = 0
    for i in record:
        if i == ".":
            temp += 1
        elif i == "*":
            temp = 0
        max_streak = max(max_streak, temp)
    count.add(max_streak)
    streak.append((max_streak, name))
print(len(count))
for num, name in streak:
    print(num, name)
