k = input()
korea = "KOREA"
ans = 0
for i in k:
    if i == korea[ans % 5]:
        ans += 1
print(ans)
