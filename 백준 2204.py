while (True):
    n = int(input())
    words = []
    if n == 0:
        break
    for _ in range(n):
        words.append(input())
        for i in range(len(words)):
            if 'A' <= words[i] or words[i] <= 'Z':
                words[i] += 32
    print(sorted(words)[0])
