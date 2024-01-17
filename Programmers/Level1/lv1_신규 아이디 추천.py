import re
import string


def solution(new_id):
    possible = list(string.ascii_lowercase) + \
        list(string.digits) + ['-', '_', '.']
    new_id = new_id.lower()
    new_id = ''.join(x for x in new_id if x in possible)
    new_id = re.sub('[.]{2,}', '.', new_id)
    new_id = new_id.strip('.')
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')
    if len(new_id) <= 2:
        new_id = new_id.ljust(3, new_id[-1])
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
