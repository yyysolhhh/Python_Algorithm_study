def solution(input_string):
    answer = ''
    str = []
    for i, ch in enumerate(input_string):
        if not str or str[-1] != ch:
            if ch in str and ch not in answer:
                answer += ch
            str.append(ch)
    if not answer:
        return "N"
    return ''.join(sorted(answer))
