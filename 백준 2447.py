
def stars(x):
    global Map
    if x == 3:
        for _ in range(x):
            for i in range(3):
                for j in range(3):
                    if (i == 1 and j == 1):
                        continue
                    else:
                        Map[i][j] = 1
        return Map

    a = x // 3
    stars(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]


N = int(input())

Map = [[0 for _ in range(N)] for _ in range(N)]
stars(N)

for i in Map:
    for j in i:
        if j == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 다른 사람 코드
# stars(N)

# # 별 찍는 재귀 함수
# def draw_star(n):
#     global Map

#     if n == 3:
#         Map[0][:3] = Map[2][:3] = [1]*3
#         Map[1][:3] = [1, 0, 1]
#         return

#     a = n//3
#     draw_star(n//3)
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             for k in range(a):
#                 Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]  # 핵심 아이디어


# N = int(input())

# # 메인 데이터 선언
# Map = [[0 for i in range(N)] for i in range(N)]

# draw_star(N)

# for i in Map:
#     for j in i:
#         if j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
