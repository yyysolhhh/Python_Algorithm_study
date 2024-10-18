k = input()
for i in range(1, len(k) - 1):
    if int(k[i]) - int(k[i - 1]) != int(k[i + 1]) - int(k[i]):
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        break;
else:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
