N = int(input())
member = []
for i in range(N):
    member.append([i, input().split()])
member.sort(key=lambda x: (-int(x[1][0]), x[0]))
for j in member:
    print(j[1][0], j[1][1])
