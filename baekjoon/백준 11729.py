N = int(input())


def hanoi_K(n):
    if n == 1:
        return 1
    return (hanoi(n - 1) * 2 + 1)


def hanoi_process(n):


print(hanoi_K(N))