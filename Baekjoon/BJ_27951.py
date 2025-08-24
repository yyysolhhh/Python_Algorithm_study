import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
U, D = map(int, input().split())

# 1 틀림
#ans = True
#res = []
#for i in A:
#    if i == 1:
#        if U > 0:
#            U -= 1
#            res.append("U")
#        else:
#            ans = False
#            break
#    elif i == 2:
#        if D > 0:
#            D -= 1
#            res.append("D")
#    elif i == 3:
#        if U > 0:
#            U -= 1
#            res.append("U")
#        elif D > 0:
#            D -= 1
#            res.append("D")
#        else:
#            ans = False
#if ans:
#    print("YES")
#    print("".join(res))
#else:
#    print("NO")

# 2 100점
top = A.count(1)
bottom = A.count(2)
both = A.count(3)
if U < top or D < bottom:
    print("NO")
else:
    print("YES")
    remaining_top = U - top
    res = []
    for i in A:
        if i == 1:
            res.append("U")
        elif i == 2:
            res.append("D")
        elif i == 3:
            if remaining_top > 0:
                res.append("U")
                remaining_top -=1
            else:
                res.append("D")
    print("".join(res))
