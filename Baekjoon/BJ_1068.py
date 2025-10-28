import sys
from collections import deque
input = sys.stdin.readline

# 2
N = int(input())
parent = list(map(int, input().split()))
erase = int(input())
child = [[] for _ in range(N)]
for i in range(N):
    if parent[i] == -1:
        root = i
        continue
    child[parent[i]].append(i)

def bfs():
    if root == erase:
        return 0
    cnt = 0
    q = deque([root])
    while q:
        cur = q.popleft()
        is_leaf = 1
        for nxt in child[cur]:
            if nxt == erase:
                continue
            is_leaf = 0
            q.append(nxt)
        cnt += is_leaf
    return cnt

print(bfs())

# 1
#def bfs(node):
#    if parents[node] == -1:
#        return 0
#    ans = len(leaf)
#    if node in leaf:
#        ans -= 1
#    q = deque([node])
#    while q:
#        cur = q.popleft()
#        for nxt in adj[cur]:
#            if nxt in leaf:
#                ans -= 1
#            q.append(nxt)
#    if len(adj[parents[node]]) == 1:
#        ans += 1
#    return ans
#
#N = int(input())
#parents = list(map(int, input().split()))
#erase = int(input())
#adj = [[] for _ in range(N)]
#outdegree = [0 for _ in range(N)]
#for i in range(N):
#    if parents[i] == -1:
#        continue
#    adj[parents[i]].append(i)
#    outdegree[parents[i]] += 1
#leaf = []
#for i in range(N):
#    if outdegree[i] == 0:
#        leaf.append(i)
#print(bfs(erase))
#
