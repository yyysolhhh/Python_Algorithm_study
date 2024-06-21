# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 87% - empty array
def solution(A, K):
    while K > 0:
        A.insert(0, A.pop())
        K -= 1
    return A

# 100%
def solution(A, K):
    while K > 0:
        if A:
            A.insert(0, A.pop())
        K -= 1
    return A

