A, B = map(int, input().split())
quotient = A // B
remainder = A % B
if A != 0 and remainder < 0:
    quotient += 1
    remainder -= B
print(quotient)
print(remainder)
