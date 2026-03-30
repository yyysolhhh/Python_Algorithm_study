# 1 틀림
#para = []
#l = 0
#ans = ""
#while True:
#    para.extend(input().strip().split())
#    if "E-N-D" in para:
#        break
#for w in para[:-1]:
#    if l < len(w):
#        ans = w
#        l = len(w)
#print(ans.lower())

# 2
import re

para = []
while True:
    try:
        para.extend(re.findall(r"[a-zA-Z-]+", input().strip()))
    except EOFError:
        break
ans = ""
l = 0
for w in para[:-1]:
    if w == "E-N-D":
        continue
    if l < len(w):
        ans = w
        l = len(w)
print(ans.lower())
