def check(first, i):
    for j in range(len(first)):
        if i == first[j]:
            return first[j+1:]


num = input()
first = ''
n = 0
while len(first) < 3000:
    n += 1
    first += str(n)

for i in num:
    print(check(first, i))
