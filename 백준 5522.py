# 1 72ms
A = 0
for _ in range(5):
    A += int(input())
print(A)

# 2 68ms
A = []
for _ in range(5):
    A.append(int(input()))
print(sum(A))
