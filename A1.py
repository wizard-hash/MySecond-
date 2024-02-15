def delete (x):
 del x[0]
 del x[-1]
ls = [1,3,2,44,5,6]
ls.sort()
print(ls)
t = open('new.txt')
for c in t:
 if c.startswith('From'):
  print(c)
