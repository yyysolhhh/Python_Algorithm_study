import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 1 시간 초과
# pokemon = {}
# for i in range(1, N+1):
#     pokemon[i] = input().rstrip()
# for _ in range(M):
#     Q = input().rstrip()
#     if Q.isdigit():
#         print(pokemon[int(Q)])
#     elif Q.isalpha():
#         print(*[i for i, j in pokemon.items() if j == Q])

# 2 맞음 (256ms)
poke_name = []
poke_num = {}
for i in range(1, N+1):
    pokemon = input().rstrip()
    poke_name.append(pokemon)
    poke_num[pokemon] = i
for _ in range(M):
    Q = input().rstrip()
    if Q.isdigit():
        print(poke_name[int(Q)-1])
    elif Q.isalpha():
        print(poke_num[Q])

# 3 2번보다 시간 많이 걸림 (276ms)
poke_name = {}
poke_num = {}
for i in range(1, N+1):
    pokemon = input().rstrip()
    poke_name[i] = pokemon
    poke_num[pokemon] = i
for _ in range(M):
    Q = input().rstrip()
    if Q.isdigit():
        print(poke_name[int(Q)])
    elif Q.isalpha():
        print(poke_num[Q])
