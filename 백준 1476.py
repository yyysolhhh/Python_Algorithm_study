E, S, M = map(int, input().split())
year = 1
ep, sp, mp = 1, 1, 1
while True:
    if ep == E and sp == S and mp == M:
        break
    ep += 1
    sp += 1
    mp += 1
    year += 1
    if ep > 15:
        ep -= 15
    if sp > 28:
        sp -= 28
    if mp > 19:
        mp -= 19
print(year)
