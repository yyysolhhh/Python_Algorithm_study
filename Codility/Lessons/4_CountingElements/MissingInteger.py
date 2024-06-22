# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 55%
def solution(A):
    A.sort()
    if max(A) < 1:
        return 1
    for i in range(1, len(A)):
        if A[i] <= 1:
            continue
        if A[i] - A[i - 1] > 1:
            return A[i - 1] + 1
    return A[-1] + 1

# 100%
def solution(A):
    numbers = [0 for _ in range(1000001)]
    for i in A:
        if i >= 0:
            numbers[i] = 1
    for i in range(1, len(numbers)):
        if not numbers[i]:
            return i
