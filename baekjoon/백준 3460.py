T = int(input())
for i in range(T):
    n = int(input())
    b = []
    a = n*2
    while(a//2 != 0):
        a = a//2
        if a % 2 == 1:
            b.append(1)
        else:
            b.append(0)
    for j in range(len(b)):
        if b[j] == 1:
            print(j, end=' ')

# T = int(input())
# for _ in range(T):
#     N = bin(int(input()))[2:]
#     print(N)
#     for i in range(len(N)):
#         if N[-i-1] == '1':
#             print(i, end=' ')
