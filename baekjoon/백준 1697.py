from collections import deque
import sys


def bfs(N):
    queue = deque([N])
    while (queue):
        # 1. 큐에서 꺼내기
        curr = queue.popleft()
        # 2. 목적지인가?
        if curr == K:
            return (visited[curr])
        # 3. 연결된 곳 순회
        for i in (curr - 1, curr + 1, curr * 2):
            # 4. 갈 수 있는가?
            if 0 <= i <= max and not visited[i]:
                # 5. 체크인
                visited[i] = visited[curr] + 1
                # 6. 큐에 넣음
                queue.append(i)


input = sys.stdin.readline
N, K = map(int, input().split())
max = 10 ** 5
visited = [0 for _ in range(max + 1)]

print(bfs(N))
