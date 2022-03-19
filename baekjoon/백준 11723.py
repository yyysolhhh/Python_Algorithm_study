import sys
input = sys.stdin.readline


def operate(S, op, num):
    if op == 'add':
        S.add(num)
    elif op == 'remove':
        S.discard(num)
    elif op == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)


M = int(input())
S = set()
for _ in range(M):
    operation = input().split()
    if len(operation) == 1:
        if operation[0] == 'all':
            S = {i for i in range(1, 21)}
        elif operation[0] == 'empty':
            S = set()
    else:
        operate(S, operation[0], int(operation[1]))
    print(S)
