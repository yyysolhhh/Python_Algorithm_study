N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
sum, num = 0, 0
for i in list(reversed(A)):
    if i < K:
        while sum <= K:
            if sum + i > K:
                break
            sum += i
            num += 1
            # print(i, sum, num)
print(sum, num)
