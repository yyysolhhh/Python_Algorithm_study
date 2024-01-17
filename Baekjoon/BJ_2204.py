while True:
    n = int(input())
    words = []
    order = {}
    if n == 0:
        break
    for _ in range(n):
        words.append(input())
    print(sorted(words, key=str.lower)[0])
