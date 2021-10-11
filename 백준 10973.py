# 뒤에서부터 오면서 앞 수가 더 큰 쌍을 찾고 그 쌍의 앞 수보다 작은 수를 뒤에서부터 찾아 그 앞 수와 swap하고 뒷부분을 내림차순으로 정렬한다.
# 이전 순열을 찾으면 first = False로 바꾸고 첫 순열일 경우 -1을 출력한다.
N = int(input())
perm = list(map(int, input().split()))
first = True
for i in range(N-1, 0, -1):
    if perm[i] < perm[i-1]:
        for j in range(N-1, i-1, -1):
            if perm[i-1] > perm[j]:
                perm[i-1], perm[j] = perm[j], perm[i-1]
                perm[i:] = sorted(perm[i:], reverse=True)
                break
        print(*perm)
        first = False
        break
if first:
    print(-1)
