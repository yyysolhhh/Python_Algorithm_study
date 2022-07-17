T = int(input())
A = [[0 for i in range(10)]for i in range(T)]
for i in range(T):
    A[i] = list(map(int, input().split()))
N = 3
print(A)
for i in range(T):
    for j in range(len(A)):
        if A[i][j] < A[i][j+1]:
            A[i][j], A[i][j+1] = A[i][j+1], A[i][j]
for i in range(T):
    print(A[i][2])
