# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 50% - timeout error
def solution(A):
    count = 0
    for i, d in enumerate(A):
        if not d:
            count += sum(A[i:])
    return count

# 50% - timeout error
def solution(A):
    count = 0
    for i, d in enumerate(A):
        if not d:
            count += sum(A[i:])
            if count > 1000000000:
                return -1
    return count

# 100%
def solution(A):
    count = 0
    east = 0
    for i, d in enumerate(A):
        if not d:
            east += 1
        else:
            count += east
            if count > 1000000000:
                return -1
    return count

