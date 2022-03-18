num = list(map(int, input().split()))
# 1
asc = False
des = False
for i in range(len(num)-1):
    if num[i] < num[i+1]:
        asc = True
    elif num[i] > num[i+1]:
        des = True
if asc and des:
    print('mixed')
else:
    if asc:
        print('ascending')
    elif des:
        print('descending')

# 2
if num == sorted(num):
    print("ascending")
elif num == sorted(num, reverse=True):
    print("descending")
else:
    print("mixed")
