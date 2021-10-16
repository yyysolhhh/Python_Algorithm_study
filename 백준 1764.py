import sys
input = sys.stdin.readline

N, M = map(int, input().split())
not_heard = set()
not_seen = set()
result = set()

for _ in range(N):
    not_heard.add(input().rstrip())

for _ in range(M):
    not_seen.add(input().rstrip())

# 1
# for i in not_heard:
#     if i in not_seen:
#         result.add(i)

# 2 교집합
result = not_heard & not_seen

print(len(result))
for i in sorted(result):
    print(i)
