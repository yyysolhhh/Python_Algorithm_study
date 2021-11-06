def fibonacci(n, cnt0, cnt1):
    if n == 0:
        cnt0 += 1
        return cnt0, cnt1
    elif n == 1:
        cnt1 += 1
        return cnt0, cnt1
    else:
        return fibonacci(n-1, cnt0, cnt1) + fibonacci(n-2, cnt0, cnt1)


T = int(input())
for _ in range(T):
    N = int(input())
    cnt0 = 0
    cnt1 = 0
    print(fibonacci(N, cnt0, cnt1))
