def solution(answers):
    supoza = [0, 0, 0]
    winner = []
    n1 = [x for x in range(1, 6)]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == n1[i % len(n1)]:
            supoza[0] += 1
        if answers[i] == n2[i % len(n2)]:
            supoza[1] += 1
        if answers[i] == n3[i % len(n3)]:
            supoza[2] += 1
    for i in range(len(supoza)):
        if (supoza[i] == max(supoza)):
            winner.append(i + 1)
    return winner


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
