def operate(S, op, num):
    if op == 'add':
        if num not in S:
            S.append(num)

    elif op == 'remove':
        if num in S:
            S.remove(num)

    elif op == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.append(num)


M = int(input())
S = []
for _ in range(M):
    operation = input().split()
    if operation[0] == 'all':
        S = [i for i in range(1, 21)]
    elif operation[0] == 'empty':
        S = []
    else:
        operate(S, operation[0], operation[1])
    print(S)
