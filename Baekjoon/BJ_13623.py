# 1
A, B, C = map(int, input().split())
if A != B and A != C:
    print("A")
elif B != A and B != C:
    print("B")
elif C != A and C != A:
    print("C")
else:
    print("*")

# 2
A, B, C = map(int, input().split())
if A == B == C:
    print("*")
elif A == B:
    print("C")
elif A == C:
    print("B")
else:
    print("A")
