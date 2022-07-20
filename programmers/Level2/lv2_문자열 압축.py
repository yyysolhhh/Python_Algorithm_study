from re import template


def solution(s):
    ans = len(s)
    for i in range(1, len(s)):
        temp = []
        tmp_len = len(s)
        for j in range(0, len(s), i):
            temp.append(s[j:j + i])
        for i in range(len(temp) - 1):
            cnt = 1
            if temp[i] == temp[i + 1]:
                tmp_len -= len(temp[i + 1])
                cnt += 1
            if cnt != 1:
                tmp_len += len(str(cnt))
        ans = min(ans, tmp_len)
    return ans


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
