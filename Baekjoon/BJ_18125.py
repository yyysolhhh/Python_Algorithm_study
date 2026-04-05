R, C = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(C)]
stu = [list(map(int, input().split())) for _ in range(R)]
ans = True
for i in range(C):
    for j in range(R):
        if pic[i][j] != stu[j][C - i - 1]:
            ans = False
            break
if ans:
    print("""|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|""")
else:
    print("""|>___/|     /}
| O O |    / }
( =0= )\""\""  \\
| ^  ____    |
|_|_/    ||__|""")
