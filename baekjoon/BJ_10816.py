import sys
input = sys.stdin.readline
N = int(input())
card = sorted(map(int, input().split()))
M = int(input())
cardToCount = list(map(int, input().split()))
result = {}

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


# 틀림 - 왜 틀렸지
for i in cardToCount:
    start = 0
    end = len(card) - 1
    if i not in result:
        result[i] = binary(i, card, start, end)
print(' '.join(map(str, result.values())))
print(*result.values())
print(' '.join(str(result[x]) if x in result else '0' for x in cardToCount))

# 맞음
for i in card:
    start = 0
    end = len(card) - 1
    if i not in result:
        result[i] = binary(i, card, start, end)
print(' '.join(str(result[x]) if x in result else '0' for x in cardToCount))

# 다른 방법
for i in card:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(*(result[x] if x in result else 0 for x in cardToCount))
