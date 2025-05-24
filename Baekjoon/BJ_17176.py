N = int(input())
nums = list(map(int, input().split()))
line = input()
ans = "y"
alp = [0 for i in range(53)]
for i in nums:
    alp[i] += 1
for i in line:
    if i == " ":
        n = 0
    elif i.isupper():
        n = ord(i) - ord("A") + 1
    else:
        n = ord(i) - ord("a") + 27
    if alp[n]:
        alp[n] -= 1
    else:
        ans = "n"
print(ans)
