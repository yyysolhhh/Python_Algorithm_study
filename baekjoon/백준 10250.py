import sys
T = int(input())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    # for i in range(W):
    #     if (N <= H * i):
    #         print((N - H * (i-1)) * 100 + i)
    #         break
    #     else:
    #         continue

    # 2
    if (N % H == 0):
        print(H * 100 + N // H)
    else:
        print((N % H) * 100 + N // H + 1)
