import sys
input = sys.stdin.readline
N = int(input())
card = list(map(int, input().split()))
M = int(input())
cardToCount = list(map(int, input().split()))

for i in cardToCount:
    print(card.count(i), end=' ')
