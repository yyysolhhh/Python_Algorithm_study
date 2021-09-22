import sys
input = sys.stdin.readline
N = int(input())
card = sorted(map(int, input().split()))
M = int(input())
cardToCount = list(map(int, input().split()))
# 시간 초과
# result = []
# for i in cardToCount:
#     print(card.count(i), end=' ')

# 이분탐색


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
print(' '.join(map(str, result.values())))
