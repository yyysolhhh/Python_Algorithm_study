# 시간 초과
# def solution(arr):
#     i = 0
#     while i < len(arr) - 1:
#         if arr[i] == arr[i + 1]:
#             del arr[i]
#         else:
#             i += 1
#     return (arr)

def solution(arr):
    stack = [arr.pop(0)]
    for i in arr:
        if stack[-1] != i:
            stack.append(i)
    return stack


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
