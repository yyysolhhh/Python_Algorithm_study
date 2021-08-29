import sys
# 내 풀이: 일단 팩토리얼 구하고 뒤집어서 0개수 구함
N = int(input())
factorial = 1
for i in range(1, N+1):
    factorial *= i
fac_str = list(reversed(str(factorial)))
for j in range(len(fac_str)):
    if int(fac_str[j]) != 0:
        print(j)
        break

# 다른 사람 풀이: 2, 5가 곱해진 개수가 0의 개수
input = sys.stdin.readline
N = int(input())
count = 0  # 0 개수
while N >= 5:  # N이 5 이상이면 5로 나눈 몫이 0 개수
    count += N // 5
    N //= 5  # 2개 증가
print(count)
