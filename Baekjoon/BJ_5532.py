L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A % C != 0:
    korean = A // C + 1
else:
    korean = A // C
if B % D != 0:
    math = B // D + 1
else:
    math = B // D
hwd = max(korean, math)
day = L - hwd
print(day)
