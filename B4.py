import re
x = open('NEw.txt')
for y in x :
 y = y.strip()
 if re.search('From:',x):
  print(x)
