# def solution(id_list, report, k):
#     answer = [0 for _ in range(len(id_list))]
#     reported_num = {}
#     report = list(set(report))
#     for i in range(len(id_list)):
#         reported_num[id_list[i]] = 0
#     for i in range(len(report)):
#         for j in range(len(report[i])):
#             if (report[i][j] == ' '):
#                 reported_num[report[i][j + 1:]] += 1
#     for i in range(len(report)):
#         for j in range(len(report[i])):
#             if (report[i][j] == ' '):
#                 if (reported_num[report[i][j + 1:]] >= k):
#                     for z in range(len(id_list)):
#                         if id_list[z] == report[i][:j]:
#                             answer[z] += 1
#                             break
#                 break
#     return answer


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    # reported_num = {x: 0 for x in id_list}
    reported_num = dict.fromkeys(id_list, 0)
    for i in set(report):
        reported_num[i.split()[1]] += 1
    for i in set(report):
        if (reported_num[i.split()[1]] >= k):
            answer[id_list.index(i.split()[0])] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con",
                                 "ryan con", "ryan con", "ryan con"], 3))
