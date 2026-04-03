import sys
input = sys.stdin.readline
N = int(input())
A, B, C, D = map(int, input().split())
S = input().strip()
ans = "Yes"
if not S[0] == S[-1] == "a":
    ans = "No"
for i in range(N - 1):
    if S[i] == S[i + 1]:
        ans = "No"
        break
if A < S.count("a") or B < S.count("b") or C < S.count("c") or D < S.count("d"):
    ans = "No"
print(ans)
