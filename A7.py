q = input('file namr ')
w = open(q)
for e in w:
 for r in e:
  if e.startswith('From') :
   print(e)
   print(r.startswith('@'))
m = [1,2]
x,y=m
print('x is ',x ,'y is ' ,y)

