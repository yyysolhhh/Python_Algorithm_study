# 1
#A, B = map(int, input().split())
#C = int(input())
#B += C
#if B >= 60:
#    A += B // 60
#    B %= 60
#if A >= 24:
#    A %= 24
#print(A, B)

# 2
A, B = map(int, input().split())
C = int(input())
total_min = A * 60 + B + C
h = (total_min // 60) % 24
m = total_min % 60
print(h, m)

