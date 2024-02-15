import re

x = 'hello $5.00 dollars'
t =re.findall('\$[0-9.]+',x)
print(t)
print(dir(re))
print(help(re.A))
