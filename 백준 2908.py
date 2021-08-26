A, B = input().split()
for i in range(2, -1, -1):
    if int(A[i]) < int(B[i]):
        print(B[::-1])
        break
    elif int(A[i]) > int(B[i]):
        print(A[::-1])
        break
    else:
        continue
