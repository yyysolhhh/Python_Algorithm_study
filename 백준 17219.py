import sys
input = sys.stdin.readline
N, M = map(int, input().split())
site = []
add = []
for _ in range(N):
    site.append(input().split())
site_dict = dict(site)
for _ in range(M):
    add = input().rstrip()
    print(site_dict[add])
