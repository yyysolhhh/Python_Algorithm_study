N = int(input())
word = list(input() for _ in range(N))
word = sorted(set(word))
l = []
for i in word:
    l.append(len(i))
while l:
    print(word[l.index(min(l))])
    word.pop(l.index(min(l)))
    l.remove(min(l))
