import sys
bra = sys.stdin.readline().strip()
stick = []
open = []
for i in range(len(bra)):
    if bra[i:i+2] == '((':
        stick.append(1)
        open.append(True)
        # print('((', stick, open)
    elif bra[i:i+2] == '()':
        for j in range(len(stick)):
            if open[j]:
                stick[j] += 1
        # print('()', stick, open)
    elif bra[i:i+2] == '))':
        for j in range(len(open)-1, -1, -1):
            if open[j]:
                open[j] = False
                break
        # print('))', stick, open)
print(sum(stick))
