def is_sqrt(n):
  i = 0
  while i * i < n:
    i += 1
  if i * i == n:
    return (1)
  else:
    return (0)
  
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
      if (is_sqrt(i)):
        answer -= i
      else:
        answer += i
    return (answer)