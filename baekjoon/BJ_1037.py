# 진짜 약수의 가장 큰 값과 가장 작은 값을 곱해준다.
num = int(input())
divisor = sorted(map(int, input().split()))
print(divisor[0] * divisor[-1])
