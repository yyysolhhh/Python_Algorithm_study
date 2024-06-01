# def binary_search(start, end):
#    mid = (start + end) // 2
#    if start > end:
#        return mid
#    temp_n = L * W * H // mid ** 3
#    if temp_n == N:
#        return mid
#    elif temp_n > N:
#        binary_search(mid + 1, end)
#    else:
#        binary_search(start, mid - 1)

# def binary_search(start, end):
#   mid = (start + end) / 2
#   if start > end:
#       print(1, mid)
#       return mid
#   vol =  mid ** 3 * N
#   if vol == max_vol:
#       print(2, mid)
#       return mid
#   elif vol < max_vol:
#       binary_search(mid, end)
#   else:
#       binary_search(start, mid)
#
# N, L, W, H = map(int, input().split())
# max_vol = L * W * H
# start = 1
# end = min(L, W, H)
# print(binary_search(start, end))

def binary_search(start, end):
    for _ in range(100):
        mid = (start + end) / 2
        cnt = (L // mid) * (W // mid) * (H // mid)
        if cnt < N:
            end = mid
        else:
            start = mid
    return end


N, L, W, H = map(int, input().split())
# start, end = 1, min(L, W, H)
start, end = 1, max(L, W, H)
print("%.10f" % binary_search(start, end))
# print(binary_search(start, end))
