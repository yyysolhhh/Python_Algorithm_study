import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pokemon = {}
for i in range(1, N+1):
    pokemon[i] = input().rstrip()
for _ in range(M):
    Q = input().rstrip()
    if Q.isdigit():
        print(pokemon[int(Q)])
    elif Q.isalpha():
        print(*[i for i, j in pokemon.items() if j == Q])
