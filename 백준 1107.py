N = list(map(int, input()))
M = int(input())
broken_button = list(map(int, input().split()))
print(N, broken_button)
channel = 100
result = 0
# while channel != N:
if channel == N:
    print(result)
else:
    result += len(N)
    for i in range(len(N)):
        if N[i] in broken_button:
            result += 1
