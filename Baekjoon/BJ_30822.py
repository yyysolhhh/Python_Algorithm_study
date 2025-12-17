# 1 - KeyError
n = int(input())
S = input()
letter = {l: 0 for l in S}
for i in S:
    letter[i] += 1
print(min(letter["u"], letter["o"], letter["s"], letter["p"], letter["c"]))

# 2
n = int(input())
S = input()
cnt = [S.count(i) for i in "uospc"]
print(min(cnt))
