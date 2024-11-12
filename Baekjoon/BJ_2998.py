# 1
b = int(input(), 2)
print(oct(b)[2:])

# 2
o = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
b = input()
while len(b) % 3 != 0:
    b = '0' + b
ans = ''
for i in range(0, len(b), 3):
    ans += o[b[i:i + 3]]
print(ans)
