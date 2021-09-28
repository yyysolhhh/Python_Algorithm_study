X = int(input())
# 시간 초과
# n = 1
# order = 1
# denom = 1
# numer = 1
# while order < X:
#     n += 1
#     for i in range(1, n+1):
#         if order == X:
#             break
#         denom = i
#         numer = n + 1 - i
#         order += 1
# print('%d/%d' % (denom, numer))

# 2
line = 1
cnt = 1
up = 1
down = line
while cnt < X:
    if (line + 1) * line / 2 <= cnt:
        line += 1
        up = 1
        down = line
        cnt += 1
        continue
    cnt += 1
    up += 1
    down -= 1
print(up, '/', down, sep='')
