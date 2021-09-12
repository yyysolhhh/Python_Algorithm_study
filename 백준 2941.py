changed = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = list(input())
result = 0
while word:
    if ''.join(word[0:2]) in changed:
        result += 1
        for _ in range(2):
            word.pop(0)
    elif ''.join(word[0:3]) in changed:
        result += 1
        for _ in range(3):
            word.pop(0)
    else:
        result += 1
        word.pop(0)
print(result)
