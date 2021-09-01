import sys


def gcd([a, b]):
    while b != 0:
        a, b = b, a % b
    return a


t = int(sys.stdin.readline())
for _ in range(t):
    n = list(map(int, sys.stdin.readline().split())))
    combi=[[] for _ in range()]
    gcd_list=[]

    for i in range(len(combi)):
      gcd_list.append(gcd(combi[i]))
    gcd_list=set(gcd_list)
    print(gcd_list)
