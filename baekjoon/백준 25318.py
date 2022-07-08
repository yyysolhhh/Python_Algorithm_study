import sys
from datetime import datetime, timedelta

input = sys.stdin.readline

# 1. 틀림

# class Opinion:
#     def __init__(self, date, time, l):
#         self.date = date + time
#         self.l = l


# N = int(input())
# if N == 0:
#     print(0)
#     exit(0)
# else:
#     opinions = []
#     p = []
#     x = 0

#     for _ in range(N):
#         date, time, l = input().split()
#         opinions.append(Opinion(date, time, l))
#     tn = datetime.strptime(opinions[-1].date, '%Y/%m/%d%H:%M:%S')
#     for i in range(N):
#         datediff = datetime.timestamp(tn) - datetime.timestamp(datetime.strptime(
#             opinions[i].date, '%Y/%m/%d%H:%M:%S'))
#         p.append(max(0.5 ** (round(datediff /
#                                    (24 * 60 * 60 * 365), 3)), 0.9 ** (N - i - 1)))
#     for i, pi in enumerate(p):
#         x += pi * int(opinions[i].l)
#     print(round(x / sum(p)))
#     # x = round(x / sum(p), 0)
#     # print(int(x))

# 2 맞음

N = int(input())

if N == 0:
    print(0)
else:
    dates = []
    l = []
    denominator = 0
    numerator = 0

    for _ in range(N):
        temp = input().split()
        year, month, day = map(int, temp[0].split('/'))
        hour, minute, second = map(int, temp[1].split(':'))
        l.append(int(temp[2]))
        dates.append(datetime(year, month, day, hour, minute, second))

    tn = dates[-1]
    for i in range(len(dates)):
        time_diff = (tn - dates[i]) / timedelta(days=365)
        pi = max(0.5 ** time_diff, 0.9 ** (N - i - 1))
        numerator += pi * l[i]
        denominator += pi

    print(round(numerator / denominator))
