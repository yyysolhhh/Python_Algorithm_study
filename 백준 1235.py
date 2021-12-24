N = int(input())
students = []
for _ in range(N):
    students.append(input())
for i in range(1, 100):
    std_temp = []
    for j in range(N):
        std_temp.append(students[j][-i:])
    if len(set(std_temp)) < N:
        continue
    else:
        print(i)
        break
