N = int(input())
steps = 1
rooms = 1
while N > rooms:
    rooms += 6 * steps
    steps += 1
print(steps)

# N = int(input())
# steps = 0
# rooms = 1
# while N > rooms:
#     steps += 1
#     rooms += 6 * (steps - 1)
# print(steps)
# 아래꺼 틀린 이유는 1일 때 0나와서
