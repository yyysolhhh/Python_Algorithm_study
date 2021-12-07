import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [False for _ in range(k)]
    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':   # 삽입
            # i는 max_heap과 min_heap 동기화를 위한 visted 배열의 인덱스로 쓸 key 값
            heapq.heappush(max_heap, (-1 * num, i))
            heapq.heappush(min_heap, (num, i))
            visited[i] = True
        elif op == "D":   # 삭제
            if num == 1:    # 최댓값 삭제
                # 이미 지워진 값 동기화
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif num == -1:   # 최솟값 삭제
                # 이미 지워진 값 동기화
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    # max_heap과 min_heap에 남아 있는 visited == False인 값을 삭제
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    # 최댓값, 최솟값 출력, 비어있으면 EMPTY 출력
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
