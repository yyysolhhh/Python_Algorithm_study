# 덜품
N = int(input())
A = sorted(map(int, input().split()))
print(A)
temp = []
ans = ''
for i in range(N):
    for j in range(i + 1, N):
        print(A[i], A[j])
        if A[i] % 10 == A[j] // 10:
            temp.append(A[i])
            temp.append(A[j])
            break
        elif A[j] % 10 == A[i] // 10:
            temp.append(A[j])
            temp.append(A[i])
            break
        if j == N - 1:
            temp.append(A[i])
temp = ''.join(map(str, temp))
print(temp)
for i in range(0, len(temp), 2):
    if i != 0 and temp[i] == temp[i - 1]:
        ans += temp[i + 1]
    else:
        ans += temp[i:i + 2]
print(ans)
