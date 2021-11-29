T = int(input())
seq = [0 for _ in range(100)]

# 1 내 풀이 - 80ms
seq[0:3] = [1, 1, 1]
for i in range(3, len(seq)):
    seq[i] = seq[i-2] + seq[i-3]

# 2 다른 사람 풀이 - 76ms
seq[0:5] = [1, 1, 1, 2, 2]
for i in range(5, len(seq)):
    seq[i] = seq[i-1] + seq[i-5]

for _ in range(T):
    N = int(input())
    print(seq[N-1])
