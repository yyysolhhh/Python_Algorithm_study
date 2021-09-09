while True:
    case = list(map(int, input()))
    if case == [0]:
        break
    palindrome = True
    for i in range(len(case)):
        if case[i] != case[-i-1]:
            palindrome = False
            print('no')
            break
    if palindrome:
        print('yes')
