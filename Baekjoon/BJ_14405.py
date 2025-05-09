# 1
p = ["pi", "ka", "chu"]
S = input()
i = 0
while i < len(S):
    if S[i:i + 2] in p:
        i += 2
    elif S[i: i + 3] in p:
        i += 3
    else:
        break
if i < len(S):
    print("NO")
else:
    print("YES")

# 2
S = input()
S = S.replace("pi", " ").replace("ka", " ").replace("chu", " ").strip()
print("YES" if len(S) == 0 else "NO")
