N = int(input())
P = sorted(map(int, input().split()))
t = [P[0]]
for i in range(1, N):
    t.append(t[i-1] + P[i])
print(sum(t))
