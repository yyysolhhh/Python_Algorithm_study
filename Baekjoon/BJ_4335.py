import sys
from collections import deque
input = sys.stdin.readline

def is_honest(ans, cur):
    n, a = ans
    if n > cur:
        temp = "too high"
    elif n < cur:
        temp = "too low"
    else:
        temp = "right on"
    if temp != a:
        return False
    return True

answers = deque()
while True:
    num = int(input())
    if num == 0:
        break
    ans = input().strip()
    if ans == "right on":
        cur = num
        res = True
        while answers:
            res = is_honest(answers.popleft(), cur)
            if res == False:
                break
        answers.clear()
        if res == False:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        continue
    answers.append((num, ans))
