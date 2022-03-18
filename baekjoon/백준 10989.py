import sys
input = sys.stdin.readline
N = int(input())

# 메모리 초과
# num = []
# for _ in range(N):
#     num.append(int(input()))
# for i in sorted(num):
#     print(i)

# 2
num_list = [0 for _ in range(10001)]
for _ in range(N):
    num = int(input())
    num_list[num] += 1
for i in range(len(num_list)):
    for j in range(num_list[i]):
        print(i)
