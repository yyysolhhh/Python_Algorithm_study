import sys
input = sys.stdin.readline
N = int(input())
ans = 100001
for _ in range(N):
    A, B = map(int, input().split())
    if B >= A and ans > B :
        ans = B
if ans == 100001:
    ans = -1
print(ans)
