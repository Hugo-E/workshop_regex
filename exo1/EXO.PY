import re

with open("exo1.txt", "r") as file:
    txt = file.read()

rgx = re.compile("([A-Z ])")
res = rgx.findall(txt)

for i in res:
    print(i, end = '')
print()