from collections import deque
import sys
input = sys.stdin.readline

def rotate(w1, w2):
    if len(w1) != len(w2):
        return w2
    w2 = deque(w2)
    for _ in range(len(w2)):
        w2.rotate(1)
        wt = "".join(w2)
        if w1 == wt:
            return wt
    return "".join(w2)

N = int(input())
words = [input().strip() for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        if words[i] == words[j]:
            continue
        words[j] = rotate(words[i], words[j])
print(len(set(words)))
