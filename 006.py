def max (q,w,e,r):
  x = None
  x = q
  for a in [q,w,e,r] :
#   if a > x :
 #   x = a
   if a is list:
    x = max(a)
   if a > x :
     x = a
  print(x)

max([2,4,8,4],3,4,0)
