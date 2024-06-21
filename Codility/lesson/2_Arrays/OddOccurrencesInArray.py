# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100%
def solution(A):
    sorted_A = sorted(A)
    while sorted_A and len(sorted_A) > 1:
        if sorted_A[-1] == sorted_A[-2]:
            sorted_A.pop()
            sorted_A.pop()
        else:
            return sorted_A.pop()
    return sorted_A.pop()

