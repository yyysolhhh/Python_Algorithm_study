import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
num.sort()


def mean(num):
    return round(sum(num)/len(num))
    # return sum(num)//len(num)


def median(num):
    return num[len(num)//2]


# def mode(num):
#     count = {}
#     for i in num:
#         count[i] = num.count(i)
#     count = sorted(count.items(), key=lambda x: (x[1], x[0]))
#     if len(count) > 1:
#         if count[0][1] == count[1][1]:
#             return count[1][0]
#         else:
#             return count[0][0]
#     else:
#         return count[0][0]

def mode(num):
    count = Counter(num)
    count_most = count.most_common(2)
    if len(num) > 1:
        if count_most[0][1] == count_most[1][1]:
            return count_most[1][0]
        else:
            return count_most[0][0]
    else:
        return count_most[0][0]


# def range(num):
#     return num[-1] - num[0]
def range(num):
    return max(num) - min(num)


print(mean(num))
print(median(num))
print(mode(num))
print(range(num))
