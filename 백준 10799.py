import sys
bra = sys.stdin.readline()
for i in range(len(bra)):
    if bra[i:i+2] == "((":
        print(1)
