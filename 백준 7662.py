import heapq
T = int(input())
k = int(input())
heap = []
for _ in range(T):
    for _ in range(k):
        op, num = input().split()
        if op == 'I':
            heapq.heappush(heap, int(num))
        elif op == "D":
            if heap:
                if num == '1':
                    heapq.heappop(heap)
                elif num == '-1':
                    heapq.heappop(heap)
        print(heap)
    if heap:
        print(heap[-1], heap[0])
    else:
        print('EMPTY')
