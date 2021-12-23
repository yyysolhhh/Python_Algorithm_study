A, B = map(int, input().split())
underprime = 0
prime_list = [False, False] + [True for _ in range(2, B+1)]
for i in range(2, B+1):
    if prime_list[i]:
        for j in range(i+i, B+1, i):
            prime_list[j] = False
for i in range(A, B+1):
    prime = 0
    for j in range(2, i+1):
        if prime_list[j]:
            while i % j == 0:
                i //= j
                prime += 1
    if prime_list[prime]:
        underprime += 1
print(underprime)
