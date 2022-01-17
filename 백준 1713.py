N = int(input())
total = int(input())
std = list(map(int, input().split()))
frame = {}
for i in std:
    if i in frame:
        frame[i] += 1
    else:
        if len(frame) < N:
            frame[i] = 1
        else:
            frame = sorted(frame.items(), key=lambda x: x[1])
            frame.pop(0)
            frame = dict(frame)
            frame[i] = 1
print(*sorted(frame))
