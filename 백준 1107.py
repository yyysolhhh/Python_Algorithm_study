N = int(input())    # target
M = int(input())    # broken button 개수
if M:   # M > 0일 때만 입력 받음
    broken = set(input().split())
else:
    broken = set()
result = abs(N - 100)   # +나 -로만 이동하는 경우 - 최댓값
for i in range(1000000):    # 작은 수에서 +로 올라가는 경우, 큰 수에서 -로 내려오는 경우까지 고려
    for j in str(i):    # i의 자릿수 중 broken이 있는 경우 중단
        if j in broken:
            break
    else:   # i가 버튼을 다 누를 수 있는 수인 경우 기존 답과 i의 자릿수 + i에서 target까지 거리 중 적은 수로 갱신
        result = min(result, len(str(i)) + abs(N - i))
print(result)
