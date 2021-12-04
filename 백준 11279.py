N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x > 0:
        arr.append(x)
    elif x == 0:
        if arr:
            print(max(arr))
            arr.remove(max(arr))
        else:
            print(0)
