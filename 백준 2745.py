N, B = input().split()


def baseConversion(B, N):
    decimal = 0
    N = list(N)
    for i in range(len(N), 0, -1):
        if N[-i].isalpha():
            N[-i] = ord(N[-i]) - 55
        decimal += int(N[-i]) * B ** (i - 1)
    return decimal


print(baseConversion(int(B), N))
