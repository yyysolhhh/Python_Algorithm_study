# 1 틀림
# N = int(input())
# A = sorted(map(int, input().split()))
# B = list(map(int, input().split()))
# sorted_B = sorted(B, reverse=True)
# re_A = []
# for i in B:
#     re_A.append(A[sorted_B.index(i)])
# S = sum(i * j for i, j in zip(re_A, B))
# print(S)

# 2 맞음
N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)
S = sum(i * j for i, j in zip(A, B))
print(S)
