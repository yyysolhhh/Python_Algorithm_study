N, K = input().split()
N = int(N)
K = int(K)
circle = [i for i in range(1, N+1)]
josephus = []
# order = K - 1
# while circle:
#     if order > N:
#         order = N - K - 1
#     if N == 1:
#         order = 0
#     josephus.append(str(circle.pop(order)))
#     N -= 1
#     order += K - 1
# order -> sequence로 바꿈
sequence = K - 1
print(circle)
while circle:
    print(sequence)
    if sequence >= len(circle):
        sequence = sequence % len(circle)
        # sequence = sequence - len(circle)
    else:
        josephus.append(str(circle.pop(sequence)))
        sequence += K - 1
    print(sequence, circle)

print("<" + ", ".join(josephus) + ">")
