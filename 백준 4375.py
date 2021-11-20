import sys
input = sys.stdin.readline

# 1 시간 초과
# while True:
#     try:
#         n = int(input())
#         ans = 1
#         while True:
#             if ans % n == 0:
#                 print(len(str(ans)))
#                 break
#             ans = int(str(ans) + '1')
#     except EOFError:
#         break

# 2
while True:
    try:
        n = int(input())
        ans = 1
        while True:
            if ans % n == 0:
                print(len(str(ans)))
                break
            ans = ans * 10 + 1
    except:
        break
