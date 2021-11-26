N, M = map(int, input().split())
pokemon = {}
for i in range(1, N+1):
    pokemon[i] = input()
for _ in range(M):
    Q = input()
    if Q.isalnum():
        print(pokemon[int(Q)])
    elif Q.isalpha():
        # print(pokemon.keys(Q))
        print('q')
