#1
T = int(input())
for i in range(1, T + 1):
    B = int(input())
    case = input()
    print(f"Case #{i}: ", end="")
    for b in range(0, len(case), 8):
        byte = "0b"
        for l in case[b:b + 8]:
            if l == "I":
                byte += "1"
            elif l == "O":
                byte += "0"
        print(chr(int(byte, 2)), end="")
    print()

#2
T = int(input())
for i in range(1, T + 1):
    B = int(input())
    case = input().replace("O", "0").replace("I", "1")
    ans = [chr(int(case[i:i + 8], 2)) for i in range(0, len(case), 8)]
    print(f"Case #{i}: {"".join(ans)}")
