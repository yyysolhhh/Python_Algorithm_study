N, B = input().split()


# def baseConversion(B, N):
#     decimal = 0
#     N = list(N)
#     for i in range(len(N), 0, -1):
#         if N[-i].isalpha():
#             N[-i] = ord(N[-i]) - 55
#         decimal += int(N[-i]) * B ** (i - 1)
#     return decimal

def baseConversion(B, N):
    decimal = 0
    N = list(N)
    for i in N[::-1]:
        index = N.index(i)
        if i.isalpha():
            i = ord(i) - 55
        decimal += int(i) * B ** (len(N)-index)
        print(len(N)-index, i, decimal)
    return decimal


print(baseConversion(int(B), N))
