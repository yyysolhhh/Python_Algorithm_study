S = input()
num = 0
for i in S:
    if i == " ":
        num += 1
if S[0] == " " and S[-1] == " ":
    print(num - 1)
elif S[0] == " " or S[-1] == " ":
    print(num)
else:
    print(num + 1)

# 2
# S = input().split()
# print(len(S))
