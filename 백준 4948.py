# def prime_cnt(n):
#     if n == 1:
#       return

# while True:
#     n = int(input())
#     print(prime_cnt(n))


# 1 시간 초과
while True:
    n = int(input())
    res = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if i == 2:
            res = 1
        else:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    break
            else:
                res += 1
    print(res)
