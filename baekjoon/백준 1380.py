scenario = 1
while True:
    n = int(input())
    if n == 0:
        break
    name = []
    mark_list = list(False for _ in range(n))
    for _ in range(n):
        name.append(input())
    for i in range(2*n-1):
        num, mark = input().split()
        num = int(num)
        if mark_list[num-1] == False:
            mark_list[num-1] = True
        else:
            mark_list[num-1] = False
    for i in range(len(mark_list)):
        if mark_list[i]:
            print(scenario, name[i])
    scenario += 1
