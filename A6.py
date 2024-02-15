txt = 'Arevy is a good boy'
w = txt.split()
t = list()
for x in w:
 t.append(len(x))
 t.sort(reverse= True)
res = list()
for len ,x in t:
 res.append(x)
 print(res)
