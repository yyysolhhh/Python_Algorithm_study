# 틀림
# def bonji5(n):
#     numOf5 = n // 5
#     if (n % 5) % 3 != 0:
#         return numOf5 - 1
#     else:
#         return numOf5


# N = int(input())
# numOf5 = bonji5(N)
# numOf3 = (N - (numOf5 * 5))//3
# print(numOf5, numOf3)
# if (numOf3 * 3 + numOf5 * 5 != N):
#     numOf5 -= 1
#     numOf3 = (N - numOf5*5) // 3

# elif numOf5 < 0:
#     print(-1)
# else:
#     print(numOf5 + numOf3)

N = int(input())
bonji = 0
while N >= 0:
    if N % 5 == 0:
        bonji += N // 5
        print(bonji)
        break
    N -= 3
    bonji += 1
else:
    print(-1)
