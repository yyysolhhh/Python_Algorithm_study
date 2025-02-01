# 1
form = input()
ans = 1
c, d = 26, 10
for i in range(len(form)):
    if form[i] == "c":
        if i > 0 and form[i - 1] == form[i]:
            ans *= c - 1
        else:
            ans *= c
    elif form[i] == "d":
        if i > 0 and form[i - 1] == form[i]:
            ans *= d - 1
        else:
            ans *= d
    ans %= 1000000009
print(ans)

# 2
form = input()
ans = 1
num = {"c": 26, "d": 10}
for i in range(len(form)):
    if i > 0 and form[i - 1] == form[i]:
        ans *= num[form[i]] - 1
    else:
        ans *= num[form[i]]
    ans %= 1000000009
print(ans)
