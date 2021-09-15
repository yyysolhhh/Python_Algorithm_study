N = list(map(int, input()))
M = int(input())
broken_button = list(map(int, input().split()))
print(N, broken_button)
channel = 100
result = 0
if N == channel:
    print(result)
else:
    for i in N:
        if i in broken_button:
