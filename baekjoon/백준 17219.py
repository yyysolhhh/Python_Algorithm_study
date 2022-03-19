import sys
input = sys.stdin.readline
N, M = map(int, input().split())
# 1
site = []
add = []
for _ in range(N):
    site.append(input().split())
site_dict = dict(site)
for _ in range(M):
    add = input().rstrip()
    print(site_dict[add])
# 2
site_info = {}
for _ in range(N):
    add, pss = input().split()
    site_info[add] = pss
for _ in range(M):
    site = input().rstrip()
    print(site_info[site])
