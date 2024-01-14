#n = input()
#for i in range(1, 16):
#   print(n + '*%X'%i + '=%X' %(int(n, 16) * i))

n = int(input(), 16)
for i in range(1, 16):
    print('%X*%X=%X' %(n, i, n * i))
