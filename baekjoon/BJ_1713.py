N = int(input())
total = int(input())
student = list(map(int, input().split()))
recommended = dict.fromkeys(student, 0)
frame = []

for i in student:
    print(frame, recommended)
    if i not in frame:
        frame.append(i)
        recommended[i] += 1
        if len(frame) >= N:
            min_rec = len(student)
            min_stu = frame[0]
            for j in frame:
                if recommended[j] < min_rec:
                    min_rec = recommended[j]
                    min_stu = j
            frame.remove(min_stu)
            recommended[min_stu] = 0
    else:
        recommended[i] += 1

print(' '.join(sorted(map(str, frame))))
