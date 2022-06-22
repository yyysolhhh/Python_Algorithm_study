import sys

input = sys.stdin.readline
N = int(input())
card = sorted(map(int, input().split()))
M = int(input())
question = list(map(int, input().split()))

# 시간 초과
# for i, num in enumerate(question):
#     if num in card:
#         answer[i] = 1


def binary_search(card, start, end, target):
    while (start <= end):
        mid = (start + end) // 2
        if card[mid] == target:
            return 1
        elif card[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i, num in enumerate(question):
    if binary_search(card, 0, N - 1, num):
        print(1, end=' ')
    else:
        print(0, end=' ')
