N = int(input())
member = []
# 틀림
# for i in range(N):
#     member.append([i, input().split()])
# member.sort(key=lambda x: (x[1][0], x[0]))
# for j in member:
#     print(j[1][0], j[1][1])

# 2
for i in range(N):
    member.append(list(input().split()))
member.sort(key=lambda x: int(x[0]))
for i in member:
    print(i[0], i[1])
