# 1
n = int(input())
sq = [0 for _ in range(n + 1)]
for i in range(int(n ** 0.5) + 1):
    sq[i ** 2] = 1
ans = 4
if sq[n]:
    ans = 1
else:
    for i in range(int(n ** 0.5), 0, -1):
        remain1 = n - i ** 2
        if sq[remain1] == 1:
            ans = 2
            break
        else:
            for j in range(int((n - i ** 2) ** 0.5), 0, -1):
                remain2 = n - i ** 2 - j ** 2
                if remain2 >= 0 and sq[remain2]:
                    ans = 3
                    break
print(ans)


# 2
def is_square(num):
    return num ** 0.5 == int(num ** 0.5)

n = int(input())
ans = 4
if is_square(n):
    ans = 1
else:
    for i in range(int(n ** 0.5), 0, -1):
        remain1 = n - i ** 2
        if is_square(remain1) == 1:
            ans = 2
            break
        else:
            for j in range(int((n - i ** 2) ** 0.5), 0, -1):
                remain2 = n - i ** 2 - j ** 2
                if is_square(remain2):
                    ans = 3
                    break
print(ans)
