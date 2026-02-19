past = float(input())
while True:
    temp = float(input())
    if temp == 999:
        break
    print(f"{temp - past:.2f}")
    past = temp
