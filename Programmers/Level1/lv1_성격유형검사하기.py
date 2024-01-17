# 맞음
def solution(survey, choices):
    scores = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    ans = ''
    for i, num in enumerate(choices):
        if num < 4:
            scores[survey[i][0]] += 4 - num 
        elif num > 4:
            scores[survey[i][1]] += num - 4
    if scores['R'] >= scores['T']:
        ans += 'R'
    else:
        ans += 'T'
    if scores['C'] >= scores['F']:
        ans += 'C'
    else:
        ans += 'F'
    if scores['J'] >= scores['M']:
        ans += 'J'
    else:
        ans += 'M'
    if scores['A'] >= scores['N']:
        ans += 'A'
    else:
        ans += 'N'
    print(scores)
    return ans

# 맞음
# def solution(survey, choices):
#     left_type = ['R', 'C', 'J', 'A']
#     right_type = ['T', 'F', 'M', 'N']
#     type = {'R' : (0, 0), 'T' : (0, 1), 'C' : (1, 0), 'F' : (1, 1), 'J' : (2, 0), 'M' : (2, 1), 'A' : (3, 0), 'N' : (3, 1)}
#     scores = [[0, 0] for _ in range(4)]
#     ans = ''
#     for i, num in enumerate(choices):
#         print(num, survey[i])
#         if num == 1:
#             scores[type[survey[i][0]][0]][type[survey[i][0]][1]] += 3
#         elif num == 2:
#             scores[type[survey[i][0]][0]][type[survey[i][0]][1]] += 2
#         elif num == 3:
#             scores[type[survey[i][0]][0]][type[survey[i][0]][1]] += 1
#         elif num == 5:
#             scores[type[survey[i][1]][0]][type[survey[i][1]][1]] += 1
#         elif num == 6:
#             scores[type[survey[i][1]][0]][type[survey[i][1]][1]] += 2
#         elif num == 7:
#             scores[type[survey[i][1]][0]][type[survey[i][1]][1]] += 3
#         else:
#             continue
#     for i, n in enumerate(scores):
#         if n[0] >= n[1]:
#             ans += left_type[i]
#         else:
#             ans += right_type[i]
#     return ans

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))