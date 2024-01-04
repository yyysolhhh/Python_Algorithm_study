def solution(arr1, arr2):
    result = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            result[i][j] = arr1[i][j] + arr2[i][j]
    return result

def solution2(arr1, arr2):
    result = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return result
