import re

with open("exo2.txt", "r") as file:
    txt = file.read()

# correction :   .* : *\{[^\}]*\}
# correction :   .* : *\{\s(.*=.*\s)*\}

rgx = re.compile("(.* : \{\s*.*\s*.*\s*.*\s*})")
res = rgx.findall(txt)

for i in res:
    print(i, end = '')
print()