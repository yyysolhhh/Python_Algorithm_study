# def solution(lottos, win_nums):
#     answer = []
#     zero = 0
#     score = 7
#     for i in lottos:
#         if i == 0:
#             zero += 1
#         elif i in win_nums:
#             score -= 1
#     if score == 7 and zero == 0:
#         score -= 1
#     answer.append(score - zero)
#     if score == 7:
#         score -= 1
#     answer.append(score)
#     return answer


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    score = 0
    for i in lottos:
        if i in win_nums:
            score += 1
    return ([rank[score + zero], rank[score]])


print(solution([44, 3, 2, 4, 30, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [31, 10, 45, 1, 6, 19]))
