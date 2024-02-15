class calc:
 t=0
 def __init__(self,q):
  self.q = q
  print(self.q + "thanks for redussection")

 def add (self,x,y):
  print(x+y)
 def sub(self,x,y):
  print(x-y)
 def __del__(self):
  print('oh! no I am destroyed ' + self.q)
x = calc('Aron')

x.add(9,5)
x.sub(567,8711)
x.add(7272,28373)
x = 20
