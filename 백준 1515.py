# def check(first, i):
#     for j in range(len(first)):
#         if i == first[j]:
#             return first[j+1:]


# num = input()
# first = ''
# n = 0
# while len(first) < 3000:
#     n += 1
#     first += str(n)

# for i in num:
#     print(check(first, i))

# 2
remaining = list(input())
i = 1
while remaining:
    print(i)
    for j in str(i):
        if remaining[0] == j:
            remaining.pop(0)
            break
        i += 1
    print(remaining)
print(i)
