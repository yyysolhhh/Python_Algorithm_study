# 뒤에서부터 오면서 앞 수가 더 작은 쌍을 찾고 그 쌍의 앞 수보다 큰 수를 뒤에서부터 찾아 그 앞 수와 swap하고 뒷부분을 정렬한다.
# 다음 순열을 찾으면 last = False로 바꾸고 마지막 순열일 경우 -1을 출력한다.
N = int(input())
perm = list(map(int, input().split()))
last = True
for i in range(N-1, 0, -1):
    if perm[i] > perm[i-1]:
        for j in range(N-1, i-1, -1):
            if perm[i-1] < perm[j]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm[i:] = sorted(perm[i:])
                break
        print(*perm)
        last = False
        break
if last:
    print(-1)
