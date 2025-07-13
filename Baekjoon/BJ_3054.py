# 1
l = input()
wendy, peter = "*", "#"
first = ""
second = ""
third = ""
for i, j in enumerate(l, start=1):
    frame, left = peter, peter
    if i % 3 == 0:
        frame, left = wendy, wendy
    if (i - 1) % 3 == 0 and i != 1:
        left = wendy
    first += f"..{frame}."
    second += f".{frame}.{frame}"
    third += f"{left}.{j}."
first += "."
second += "."
third += frame
print(first)
print(second)
print(third)
print(second)
print(first)

# 2
w = input()
line = [".", ".", "#", ".", "."]
for i, l in enumerate(w, 1):
    f = "#"
    if i % 3 == 0:
        f = "*"
        line[2] = line[2][:-1] + f
    line[0] += f".{f}.."
    line[1] += f"{f}.{f}."
    line[2] += f".{l}.{f}"
    line[3] += f"{f}.{f}."
    line[4] += f".{f}.."
for i in line:
    print(i)
