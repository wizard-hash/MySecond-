import glob

x = glob.glob("*.py")
print(x)
for a in x :
  b = open(a)
  print(a)
  for t in b :
 #   print(a)
    print(t)
