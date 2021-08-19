T = int(input())
for _ in range(T):
    string = input()
    sum = 0
    for i in string:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")

# 2 stack 이용
T = int(input())


def vps(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                print("NO")
                return
            else:
                stack.pop()

    if not stack:
        print("YES")
        return
    elif stack:
        print("NO")
        return


for _ in range(T):
    string = input()
    vps(string)
