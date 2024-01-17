# 시간 초과
# import sys


# def factorial(num):
#     fac = 1
#     for i in range(1, num+1):
#         fac *= i
#     return fac


# n, m = map(int, sys.stdin.readline().split())
# result = 0
# result = int(factorial(n) / (factorial(m) * factorial(n - m)))
# rev_result = list(reversed(str(result)))
# for i in range(len(rev_result)):
#     if rev_result[i] != '0':
#         print(i)
#         break

# 2 다른 사람 풀이 참고
import sys


def countNum(n, num):  # 5나 2의 개수 구하기
    count = 0
    div = num
    while n >= div:
        count += n // div
        div *= num
    return count


n, m = map(int, sys.stdin.readline().split())
result = min(countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5),
             countNum(n, 2) - countNum(m, 2) - countNum(n-m, 2))  # 분모 5의 개수 - 분자 5의 개수와 분모 2의 개수 - 분자 2의 개수 중 작은 것이 0의 개수
print(result)
