import sys
input = sys.stdin.readline
N = int(input())
T, P = [], []
case1 = 0
case2 = 0
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
for i in range(N-1, -1, -1):
    if T[i] > N - i:
        continue
    else:
        current = P[i] + max(case1, case2)
        case2 = case1
        case1 = current
print(max(case1, case2))
