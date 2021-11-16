die0, die1, die2 = list(map(int, input().split()))
if die0 == die1 == die2:
    print(10000 + die0 * 1000)
elif die0 != die1 != die2:
    print(max(die0, die1, die2) * 100)
else:
    if die0 == die1:
        print(1000 + die0 * 100)
    elif die1 == die2:
        print(1000 + die1 * 100)
    else:
        print(1000 + die0 * 100)
# elif die0 == die1 != die2 or die1 == die2 != die0 or die0 == die2 != die1:
        # print(1000 + )
