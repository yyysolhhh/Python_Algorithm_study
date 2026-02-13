T = int(input())
for _ in range(T):
    n = int(input())
    room = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if room[j]:
                room[j] = 0
            else:
                room[j] = 1
    print(sum(room[1:]))
