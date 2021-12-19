k = int(input())
signs = list(input().split())
num = [False for _ in range(9)]
min_arr = []
max_arr = []
for i in range(k):
    if signs[i] == '<':
        for i in range(len(num)):
            if not num[i]:
                min_arr.append(i)
                num[i] = True
    elif signs[i] == '>':
