import sys
bra = sys.stdin.readline()
stick = []
for i in range(len(bra)):
    if bra[i:i+2] == "((":
        while(bra[i:i+2] != "))"):
            stick.append(i)
            if bra[i:i+2]
