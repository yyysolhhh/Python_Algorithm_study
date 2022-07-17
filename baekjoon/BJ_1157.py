# import string
# word = input()
# alphabet = string.ascii_letters
# big = string.ascii_uppercase
# num = []
# for i in alphabet:
#     num.append(word.count(i))
# print(big[num.index(max(num))])

word = input()
alphabetNum = [0 for _ in range(26)]
for i in word:
    if i.islower():
        alphabetNum[ord(i)-97] += 1
    elif i.isupper():
        alphabetNum[ord(i)-65] += 1
if alphabetNum.count(max(alphabetNum)) > 1:
    best = '?'
else:
    best = chr(alphabetNum.index(max(alphabetNum))+65)
print(best)
