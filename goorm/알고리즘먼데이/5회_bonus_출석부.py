# 보너스 포함 안됨
N, k = map(int, input().split())
attendance_book = []
for _ in range(N):
    s, t = input().split()
    attendance_book.append([s, t])
attendance_book.sort(key=lambda x: (x[0], x[1]))
print(attendance_book[k - 1][0], attendance_book[k - 1][1])
