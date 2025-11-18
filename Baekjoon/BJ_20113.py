N = int(input())
X = list(map(int, input().split()))
cnt = [0 for _ in range(N + 1)]
pass_cnt = 0
for i in X:
    if i == 0:
        pass_cnt += 1
    else:
        cnt[i] += 1
if max(cnt) < pass_cnt:
    print("skipped")
else:
    ans = -1
    for i, n in enumerate(cnt[1:], start=1):
        if n == max(cnt):
            if ans == -1:
                ans = i
            else:
                ans = "skipped"
    print(ans)
