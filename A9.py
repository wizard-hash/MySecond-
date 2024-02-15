import turtle
a = dict()
#print(a)
a['one'] = 1
a['two']= 2
a['three'] = 3
print(a)
t = list(a.items())
v=t.sort()
print(t)
for c,y in t:
 print(c,y)
