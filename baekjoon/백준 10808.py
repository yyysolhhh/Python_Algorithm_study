# 내 풀이 - 아스키코드 이용 - 시간 덜 걸림
S = input()
alpha = [0 for i in range(26)]
for i in S:
    alpha[ord(i) - ord('a')] += 1
for i in alpha:
    print(i, end=' ')

# 다른 풀이 - count 이용
# import string
# S = input()
# alpha = string.ascii_lowercase
# for i in alpha:
#     num = S.count(i)
#     print(num, end=' ')
