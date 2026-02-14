def solve():
    short = "UCPC"
    idx = 0
    for i in s:
        if short[idx] == i:
            idx += 1
        if idx == 4:
            return "love"
    else:
        return "hate"

if __name__ == "__main__":
    s = input()
    print("I", solve(), "UCPC")
