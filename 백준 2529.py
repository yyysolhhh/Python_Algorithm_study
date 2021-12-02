k = int(input())
signs = list(input().split())
num = [False for _ in range(9)]
res = []
for i in range(k):
    for j in range(9):
        num[j] = True
        res.append(j)
        if signs[i] == '<':

        elif signs[i] == '>':
