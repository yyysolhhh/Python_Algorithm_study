# 틀림
T = int(input())
for _ in range(T):
    S = input()
    mark, token = input().split()
    res = ''
    n_token = token
    if len(token) < len(S):
        while len(n_token) < len(S):
            n_token += token
    if mark == 'E':
        for i in range(len(S)):
            temp = ord(S[i]) + ord(n_token[i]) % 26
            if 65 <= temp < 90 or 97 <= temp < 121:
                res += chr(temp)
            else:
                res += chr(temp - 25)
    elif mark == 'D':
        for i in range(len(S)):
            temp = ord(S[i]) - ord(n_token[i]) % 26
            if 65 < temp <= 90 or 97 < temp <= 121:
                res += chr(temp)
            else:
                res += chr(temp + 25)
    print(res)
