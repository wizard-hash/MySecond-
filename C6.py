import urllib.request
x = urllib.request.urlopen('https://bedford-computing.co.uk')
for y in x :
 print(y.decode().strip())
