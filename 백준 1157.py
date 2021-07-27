import string
word = input()
alphabet = string.ascii_letters
big = string.ascii_uppercase
num = []
for i in alphabet:
    num.append(word.count(i))
print(big[num.index(max(num))])
