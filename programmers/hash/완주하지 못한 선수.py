def solution(participant, completion):
    answer = ''

    # for i in participant:
    #     if i not in completion:
    #         answer += i
    #     else:
    #         completion.remove(i)

    # par_list = {}
    # for i in participant:
    #     par_list[i] = 0
    # for i in completion:
    #     par_list[i] = 1
    # for i, j in par_list.items():
    #     if j == 0:
    #         answer += i
    # return answer

    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i + 1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
