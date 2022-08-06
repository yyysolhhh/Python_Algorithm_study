def func(i):
    if len(arr) == 0:
        return -1
    else:
        if i == 'R':
            arr.reverse()
        elif i == 'D':
            arr.pop(0)
    return 1


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input()
    is_error = 0
    if n == 0:
        print("error")
        break
    arr = list(map(int, arr.lstrip('[').rstrip(']').split(',')))
    for i in p:
        if func(i) == -1:
            is_error = 1
            break
    if is_error == 1:
        print("error")
    else:
        print('[' + ','.join(map(str, arr)) + ']')
