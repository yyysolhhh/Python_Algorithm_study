N = int(input())
# 2 맞음 - N을 이진수로 바꿔서 각각의 자리에 3의 거듭제곱을 곱해서 더해준다.
bin = ''
ans = 0
while N > 0:
    bin += str(N % 2)
    N //= 2
for i in range(len(bin)):
    ans += int(bin[i]) * 3 ** i
print(ans)

# 1 시간 초과
# arr = [1, 3, 9]
# for i in range(N):
#     j = i + 1
#     while 3 ** i + 3 ** j < 3 ** (i+2) + 3 ** (i+1):
#         arr.append(3 ** i + 3 ** j)
#         # print(3 ** i, 3 ** j, 3 ** i + 3 ** j)
#         j += 1
# print(sorted(arr)[N-1])
