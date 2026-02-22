target = "2023"
N = int(input())
ans = 0
if N >= 2023:
    for i in range(1, N + 1):
        idx = 0
        for j in str(i):
            if target[idx] == j:
                idx += 1
            if idx == 4:
                ans += 1
                break
print(ans)
