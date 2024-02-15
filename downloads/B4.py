import re
x = open('mbox.txt')
c = 0
for y in x :
# y = y.rstrip()
# if re.search('From:',y):
 # print(y)
 z = re.findall('From .* ([0-9][0-9]):',y)
# print(z)
 if len(z)>0:
  print(z)
 c+=1
print(c)
