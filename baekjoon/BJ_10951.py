import sys
while 1:
    try:
        A, B = map(int, sys.stdin.readline().split())
    except:
        break
    print(A + B)
