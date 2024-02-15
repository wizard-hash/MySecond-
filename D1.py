class person:
 def __init__(self,fname,lname):
  self.fn = fname
  self.ln= lname
 def dis(self):
  print("your name is ",self.fn,self.ln)


class char(person):
 pass
x = char("Qron","ngn")
x.dis()
