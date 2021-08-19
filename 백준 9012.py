T = int(input())
for _ in range(T):
    string = input()
    l = 0
    r = 0
    for i in string:
        if i == "(":
            l += 1
        elif i == ")":
            r += 1
    if l == r:
        print("YES")
    else:
        print("NO")
