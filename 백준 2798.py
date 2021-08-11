import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                result = max(result, sum)
print(result)

# 2
# from itertools import combinations
# card_num, target_num = map(int, input().split())
# card_list = list(map(int, input().split()))
# biggest_num = 0
# for cards in combinations(card_list, 3):
#     temp_sum = sum(cards)
#     if biggest_num < temp_sum <= target_num:
#         biggest_num = temp_sum
# print(biggest_num)
