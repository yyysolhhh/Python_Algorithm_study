import sys


# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# 재귀함수 이용한 gcd 함수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(sys.stdin.readline())
for _ in range(t):
    num = list(map(int, sys.stdin.readline().split()))
    # combi = [[] for _ in range(len(n)**2)]
    # gcd_list = []
    # for i in range(1, len(n)-1):  # n[1]부터 조합 만드려다가 실패
    #     for j in range(len(n)):
    #         combi.append([n[j], n[j+i]])
    # print(combi)
    # for i in range(len(combi)):
    #   gcd_list.append(gcd(combi[i]))
    # gcd_list=set(gcd_list)
    # print(gcd_list)
    # 문제 잘못 이해함. 중복 제거해야 되는걸로 이해함.
    sum = 0
    n = num.pop(0)
    for i in range(n):
        for j in range(n):
            if i < j:
                sum += gcd(num[i], num[j])
    print(sum)
