# 틀림
button = ["", "1.,?!", "2ABC", "3DEF", "4GHI",
          "5JKL", "6MNO", "7PQRS", "8TUV", "9WXYZ"]
n = int(input())
s = input() + 'e'
cnt = 1
for i in range(n):
    if s[i] == s[i + 1]:
        cnt += 1
    else:
        print(button[int(s[i])][cnt - 1], end='')
        cnt = 1
