import sys
input = sys.stdin.readline
N = int(input())
word = list(input().strip() for _ in range(N))
word = sorted(set(word))
# 내 풀이
l = []
for i in word:
    l.append(len(i))
while l:
    print(word.pop(l.index(min(l))))
    l.remove(min(l))

# 다른 사람 풀이
word.sort(key=len)
for i in word:
    print(i)
