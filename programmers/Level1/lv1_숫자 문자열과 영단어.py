numbers = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]


def solution(s):
    for i in numbers:
        s = s.replace(i, str(numbers.index(i)))
    return int(s)


print(solution("one4seveneightone"))
