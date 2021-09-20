import sys
input = sys.stdin.readline
N = int(input())
card = sorted(map(int, input().split()))
M = int(input())
cardToCount = list(map(int, input().split()))
result = []
# 시간 초과
# for i in cardToCount:
#     print(card.count(i), end=' ')


def binary(i, card, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if card[mid] == i:
        return card[start:end+1].count(i)
    elif card[mid] < i:
        return binary(i, card, mid+1, end)
    else:
        return binary(i, card, start, mid-1)


result = {}
for i in cardToCount:
    start = 0
    end = len(card) - 1
    if i not in result:
        result[i] = binary(i, card, start, end)
for i in result:
    print(result[i], end=' ')
