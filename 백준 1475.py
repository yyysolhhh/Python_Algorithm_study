N = input()
one_set = [0 for i in range(10)]
# 3
for i in N:
    i = int(i)
    if i == 9:
        one_set[6] += 1
    else:
        one_set[i] += 1
if one_set[6] % 2 == 0:
    one_set[6] //= 2
else:
    one_set[6] = one_set[6] // 2 + 1
print(max(one_set))

# 2 틀림
# for i in N:
#     i = int(i)
#     if one_set[i] > 1:
#         if i == 6 and one_set[9] != one_set[6]:
#             one_set[9] += 1
#         elif i == 9 and one_set[9] != one_set[6]:
#             one_set[6] += 1
#         else:
#             one_set[i] += 1
#     else:
#         one_set[i] += 1
# print(max(one_set))

# 1 잘못 생각함
# for i in N:
#     print(one_set)
#     if i in one_set:
#         one_set.remove(i)
#     else:
#         if i == '6' and '9' in one_set:
#             one_set.remove('9')
#         elif i == '9' and '6' in one_set:
#             one_set.remove('6')
#         else:
#             res += 1
# print(res)
