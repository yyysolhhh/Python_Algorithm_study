N = int(input())
ans = "%.270f" % (1 / (2 ** N))
for i in range(len(ans) - 1, -1, -1):
    if ans[i] != '0':
        break
print(ans[:i + 1])
