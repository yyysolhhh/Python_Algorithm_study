
def bonji5(n):
    numOf5 = N // 5
    if (N % 5) % 3 != 0:
        return numOf5 - 1
    else:
        return numOf5


N = int(input())
numOf3 = (N - (bonji5(N) * 5))/3
print(int(bonji5(N) + numOf3))
