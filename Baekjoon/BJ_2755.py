grades = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
extra = {"+": 0.3, "0": 0, "-": -0.3}
N = int(input())
ans = 0
total = 0
for _ in range(N):
    name, credit, grade = input().split()
    credit = int(credit)
    if grade == "F":
        total += credit
        continue
    ans += credit * (grades[grade[0]] + extra[grade[1]])
    total += credit
ans = round(ans / total + 10 ** -10, 2)
print("%.2f" % (ans))
#print(f"{ans:.2f}")
