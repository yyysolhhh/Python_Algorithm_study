import math


# 1 - 맞음
def binary_search(start, end):
   mid = (start + end) // 2
   if start > end:
       print(mid + 1)
       return
   temp_z = math.floor(100 * (Y + mid) / (X + mid))
   if temp_z <= Z:
       binary_search(mid + 1, end)
   else:
       binary_search(start, mid - 1)


X, Y = map(int, input().split())
Z = math.floor(100 * Y / X)
MAX = 1000000000
if Z >= 99:
    print(-1)
else:
    binary_search(1, MAX)


# 2 - 맞음
#X, Y = map(int, input().split())
#Z = math.floor(100 * Y / X)
#MAX = 1000000000
#start, end = 1, MAX
#if Z >= 99:
#    print(-1)
#else:
#   while start <= end:
#       mid = (start + end) // 2
#       temp_z = math.floor(100 * (Y + mid) / (X + mid))
#       if temp_z <= Z:
#           start = mid + 1
#       else:
#           end = mid - 1
#           cnt = mid
#   print(mid, cnt)


# 3 역시나 시간초과
#cnt = 1
#original = math.floor(Y / X * 100)
#if original >= 99:
#    print -1
#else:
#    while True:
#        X += 1
#        Y += 1
#        Z = math.floor(Y / X * 100)
#        if Z > original:
#            break
#        cnt += 1
#    print(cnt)
