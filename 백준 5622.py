# 1
# Word = input()
# t = 0
# for i in Word:
#     if i == 'A' or i == 'B' or i == 'C':
#         t += 3
#     elif i == 'D' or i == 'E' or i == 'F':
#         t += 4
#     elif i == 'G' or i == 'H' or i == 'I':
#         t += 5
#     elif i == 'J' or i == 'K' or i == 'L':
#         t += 6
#     elif i == 'M' or i == 'N' or i == 'O':
#         t += 7
#     elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
#         t += 8
#     elif i == 'T' or i == 'U' or i == 'V':
#         t += 9
#     elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
#         t += 10
# print(t)

# 2
Alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
Word = input()
t = 0
for unit in Alphabet:
    for i in unit:
        for j in Word:
            if i == j:
                t += Alphabet.index(unit) + 3
print(t)
