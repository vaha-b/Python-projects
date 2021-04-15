import re

ss = input().split("|")

if re.findall(ss[0], ss[1]):

print(True)

else:

print(False)
