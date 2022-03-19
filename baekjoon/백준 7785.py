n = int(input())
log = {}
for _ in range(n):
    name, enter = input().split()
    log[name] = enter
log = sorted(log.items(), reverse=True)
for i in log:
    if i[1] == "enter":
        print(i[0])
