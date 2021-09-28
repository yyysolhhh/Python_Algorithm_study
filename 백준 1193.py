X = int(input())
n = 1
order = 1
denom = 1
numer = 1
while order < X:
    n += 1
    for i in range(1, n+1):
        if order == X:
            break
        denom = n + 1 - i
        numer = i
        order += 1
print('%d/%d' % (denom, numer))
