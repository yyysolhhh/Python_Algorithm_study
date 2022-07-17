def check_lr(n, m, ine):
    if ine == '<':
        return n < m
    elif ine == '>':
        return n > m


k = int(input())
signs = list(input().split())
visited = [0 for i in range(9)]
max_ans = ''
min_ans = ''
