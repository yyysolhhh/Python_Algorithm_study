import sys
input = sys.stdin.readline
N, M = map(int, input().split())
not_heard = []
not_seen = []
result = []
for _ in range(N):
    not_heard.append(input().rstrip())
for _ in range(M):
    not_seen.append(input().rstrip())
for i in not_heard:
    if i in not_seen:
        result.append(i)
print(len(result))
for i in sorted(result):
    print(i)
