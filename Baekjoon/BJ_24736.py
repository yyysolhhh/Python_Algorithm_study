# 1
visiting = list(map(int, input().split()))
home = list(map(int, input().split()))
score = [6, 3, 2, 1, 2]
v_score = sum(i * j for i, j in zip(visiting, score))
h_score = sum(i * j for i, j in zip(home, score))
print(v_score, h_score)

# 2
score = [6, 3, 2, 1, 2]
for _ in range(2):
    team = list(map(int, input().split()))
    print(sum(i * j for i, j in zip(team, score)), end=" ")
