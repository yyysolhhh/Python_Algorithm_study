def multiple(X, cnt):
    print(X, cnt)
    if len(X) == 1:
        if X == 3 or X == 6 or X == 9:
            print(cnt)
            return 'YES'
        else:
            print(cnt)
            return 'NO'
    Y = 0
    for i in X:
        Y += int(i)
    return multiple(str(Y), cnt+1)


X = input()
cnt = 0
print(multiple(X, cnt))
