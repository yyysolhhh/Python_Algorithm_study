from sympy import re


word = input()
result = 'z' * 50
for p1 in range(1, len(word)):
    for p2 in range(3, len(word)):
        if p1 < p2:
            temp = ""
            temp += word[p1::-1] + word[p2:p1:-1] + word[:p2:-1]
            if result > temp:
                # print(result, end=" ")
                result = temp
                # print(result)
print(result)
