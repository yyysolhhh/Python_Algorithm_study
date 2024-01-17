word = input()
word_collection = []
for p1 in range(len(word) - 2):
    for p2 in range(p1 + 1, len(word) - 1):
        temp = ""
        temp += word[p1::-1] + word[p2:p1:-1] + word[:p2:-1]
        word_collection.append(temp)
print(sorted(word_collection)[0])
