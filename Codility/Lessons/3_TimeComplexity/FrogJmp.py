# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    remains = (Y - X) % D
    if remains:
        return (Y - X) // D + 1
    else:
        return (Y - X) // D
