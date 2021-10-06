import sys
input = sys.stdin.readline
N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
num.sort()


def mean():
    return sum(num)//len(num)


def median():
    return num[len(num)//2]


def mode():
    count = {}
    for i in num:
        count[i] = num.count(i)
    count = sorted(count.items(), key=lambda x: (x[1], x[0]))
    if len(count) > 1:
        if count[0][1] == count[1][1]:
            return count[1][0]
        else:
            return count[0][0]
    else:
        return count[0][0]


def range():
    return num[-1] - num[0]


print(mean())
print(median())
print(mode())
print(range())
