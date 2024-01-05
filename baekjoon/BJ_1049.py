import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pack_price = []
unit_price = []
result = 0

for _ in range(M):
    pack, unit = map(int, input().split())
    pack_price.append(pack)
    unit_price.append(unit)
pack_price.sort()
unit_price.sort()
if (6 * unit_price[0] > pack_price[0]):
    result = min(pack_price[0] * (N // 6) + unit_price[0] * (N % 6), pack_price[0] * (N // 6 + 1))
else:
    result = unit_price[0] * N
print(result) 

# 2
#N, M = map(int, input().split())
#pack_price = []
#unit_price = []
#result = 0
#
#for _ in range(M):
#    pack, unit = map(int, input().split())
#    pack_price.append(pack)
#    unit_price.append(unit)
#pack_price.sort()
#unit_price.sort()
#result = min(pack_price[0] * (N // 6) + unit_price[0] * (N % 6), pack_price[0] * (N // 6 + 1), unit_price[0] * N)
#print(result) 

# 3 -  메모리, 시간 동일
#N, M = map(int, input().split())
#price_list = []
#result = 0
#
#for _ in range(M):
#    price = tuple(map(int, input().split()))
#    price_list.append(price)
#pack_price = sorted(price_list, key=lambda x: x[0])[0][0]
#unit_price = sorted(price_list, key=lambda x: x[1])[0][1]
#if (6 * unit_price > pack_price):
#    result = min(pack_price * (N // 6) + unit_price * (N % 6), pack_price * (N // 6 + 1))
#else:
#    result = unit_price * N
#print(result) 
