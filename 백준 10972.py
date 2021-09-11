N = int(input())
permutation = list(map(int, input().split()))
for i in range(len(permutation)):
    if permutation[i] < permutation[i+1]:
