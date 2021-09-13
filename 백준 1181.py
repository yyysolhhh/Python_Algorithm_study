import sys
input = sys.stdin.readline
N = int(input())
word = list(input().strip() for _ in range(N))
word = sorted(set(word))
l = []
for i in word:
    l.append(len(i))
while l:
    print(word.pop(l.index(min(l))))
    l.remove(min(l))
