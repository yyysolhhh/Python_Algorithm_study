S, K = input().split()
K = int(K)
S = S.upper()

# 2 - 맞음
alpha = [S[0]]
cnt = [1]
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        if S[i] != alpha[-1]:
            continue
        cnt[-1] += 1
    else:
        if S[i] in alpha:
            continue
        alpha.append(S[i])
        cnt.append(1)
for i in cnt:
    if i >= K:
        print(1, end="")
    else:
        print(0, end="")


# 1 - 틀림
#past = [S[0]]
#cnt = 1
#ans = ""
#i = 1
#while i < len(S):
#    if S[i] == S[i - 1]:
#        cnt += 1
#    else:
#        if cnt >= K:
#            print(S[i - 1], cnt, 1)
#            ans += "1"
#        else:
#            print(S[i - 1], cnt, 0)
#            ans += "0"
#        if S[i] in past:
#            while S[i] == S[i + 1]:
#                i += 1
#            print(i)
#            cnt = 0
#            continue
#        cnt = 1
#        past.append(S[i])
#    i += 1
#if cnt == 0:
#    ans += ""
#elif cnt >= K:
#    print(S[i - 1], cnt, 1)
#    ans += "1"
#else:
#    print(S[i - 1], cnt, 0)
#    ans += "0"
#print(ans)
