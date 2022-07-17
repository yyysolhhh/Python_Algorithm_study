while(True):
    try:
        string = input()
        num = [0 for _ in range(4)]
        for i in string:
            if i.islower():
                num[0] += 1
            elif i.isupper():
                num[1] += 1
            elif i.isdecimal():
                num[2] += 1
            elif i.isspace():
                num[3] += 1
        print(" ".join(map(str, num)))
    except EOFError:
        break
