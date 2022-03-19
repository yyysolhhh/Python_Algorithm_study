import sys


def push_front(x):
    deque.insert(0, x)


def push_back(x):
    deque.append(x)


def pop_front():
    if deque:
        return deque.pop(0)
    else:
        return -1


def pop_back():
    if deque:
        return deque.pop()
    else:
        return -1


def size():
    return len(deque)


def empty():
    if deque:
        return 0
    else:
        return 1


def front():
    if deque:
        return deque[0]
    else:
        return -1


def back():
    if deque:
        return deque[-1]
    else:
        return -1


N = int(sys.stdin.readline())
deque = []
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "push_front":
        x = command[1]
        push_front(x)
    elif command[0] == "push_back":
        x = command[1]
        push_back(x)
    elif command[0] == "pop_front":
        print(pop_front())
    elif command[0] == "pop_back":
        print(pop_back())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())

# 다른 사람
# def push_front(x, deq):
#     tmp = [x]
#     tmp.extend(deq)
#     deq = tmp
#     return deq

# def push_back(x, deq):
#     deq.append(x)
#     return deq

# def pop_front(deq):
#     if deq :
#         print(deq.pop(0))
#     else : #빈 리스트 == False
#         print(-1)

# def pop_back(deq):
#     if deq :
#         print(deq.pop())
#     else :
#         print(-1)

# def size(deq):
#     print(len(deq))

# def empty(deq) :
#     if not deq :
#         print(1)
#     else :
#         print(0)

# def front(deq) :
#     if deq :
#         print(deq[0])
#     else :
#         print(-1)

# def back(deq) :
#     if deq :
#         print(deq[-1])
#     else :
#         print(-1)

# statements_dict = {
#     'push_front' : push_front,
#     'push_back' : push_back,
#     'pop_front' : pop_front,
#     'pop_back' : pop_back,
#     'size' : size,
#     'empty' : empty,
#     'front' : front,
#     'back' : back
# }

# N = int(input())

# deq = []

# for _ in range(N) :
#     statement = input().split(" ")

#     if len(statement) == 1 :
#         command = statement[0]
#         statements_dict[command](deq)
#     else :
#         command, x = statement
#         deq = statements_dict[command](x, deq)
