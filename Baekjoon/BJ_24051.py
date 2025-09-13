import sys
input = sys.stdin.readline

def insertion_sort(A):
    cnt = 0
    for i in range(1, N):
        loc = i - 1;
        new = A[i]
        while loc >= 0 and new < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
            cnt += 1
            if cnt == K:
                return A[loc + 1]
        if loc + 1 != i:
            A[loc + 1] = new;
            cnt += 1
            if cnt == K:
                return A[loc + 1]
    return -1

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(insertion_sort(A))
