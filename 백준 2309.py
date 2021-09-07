tall = list(int(input()) for _ in range(9))
tall.sort()
sum_of_tall = sum(tall)
# if sum_of_tall == 100:
#     for i in tall:
#         print(i)
# elif sum_of_tall > 100:
#     diff = sum_of_tall - 100
for i in range(9):
    for j in range(i+1, 9):
        if sum_of_tall - (tall[i] + tall[j]) == 100:
            if i == j:
                continue
            tall.pop(j)
            tall.pop(i)
            break
    break
for i in tall:
    print(i)
