N = 10
while N < 100:
    if int(str(N)[::-1]) % 4 == 0:
        if (N // 10 + N % 10) % 6 == 0:
            if str(N).count("8") == 0:
                print(N)
                break
    N += 1
