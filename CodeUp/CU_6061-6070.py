# 6061
a, b = map(int, input().split())
print(a | b)

# 6062
a, b = map(int, input().split())
print(a ^ b)

# 6063
a, b = map(int, input().split())
print(a if a > b else b)

# 6064
a, b, c = map(int, input().split())
print((a if a < b else b) if (a if a < b else b) < c else c)

# 6065
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 6066
a, b, c = map(int, input().split())
for i in [a, b, c]:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')

# 6067
a = int(input())
if a < 0:
    if a % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if a % 2 == 0:
        print('C')
    else:
        print('D')

# 6068
a = int(input())
if a >= 90:
    print('A')
elif a >= 70:
    print('B')
elif a >= 40:
    print('C')
else:
    print('D')

# 6069
a = input()
if a == 'A':
    print("best!!!")
elif a == 'B':
    print("good!!")
elif a == 'C':
    print("run!")
elif a == 'D':
    print("slowly~")
else:
    print("what?")

# 6070
m = int(input())
if m // 3 == 1:
    print("spring")
elif m // 3 == 2:
    print("summer")
elif m // 3 == 3:
    print("fall")
else:
    print("winter")