remaining = list(input())
i = 1
while True:
    for j in str(i):
        if remaining and remaining[0] == j:
            remaining.pop(0)
    if not remaining:
        break
    i += 1
print(i)
