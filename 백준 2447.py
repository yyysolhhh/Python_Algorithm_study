N = int(input())


def stars(x):
    for _ in range(x):
        for i in range(1, 4):
            for j in range(1, 4):
                if (i == 2 and j == 2):
                    print(" ", end="")
                    continue
                print("*", end="")
            print()


stars(1)
