import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    result = 0
    # print(M, queue)
    while queue:
        if max(queue) != queue[0]:
            queue.append(queue.pop(0))
        else:
            queue.pop(0)
            result += 1
            if M == 0:
                break
        if M > 0:
            M -= 1
        else:
            M = len(queue) - 1
        # print(M, queue)
    print(result)
