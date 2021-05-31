import re

with open("exo2.txt", "r") as file:
    txt = file.read()

rgx = re.compile(".* : \{[^\{]\}")
res = rgx.findall(txt)

for i in res:
    print(i)
txt = rgx.sub('', txt)
txt = re.sub("#[^\n]*", '', txt)
rgx = re.compile("^[\s]*$")

if rgx.match(txt):
    print("No error")
else:
    print("Error")