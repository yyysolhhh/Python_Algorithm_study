n = int(input())
rand = list(map(int, input().split()))
for i in rand[-1::-1]:
    print(i, end=' ')
