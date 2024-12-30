N = int(input())
gom = set()
ans = 0
for _ in range(N):
    name = input()
    if name != "ENTER":
       gom.add(name)
    else:
        ans += len(gom)
        gom.clear()
ans += len(gom)
print(ans)
