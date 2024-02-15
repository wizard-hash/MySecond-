import urllib.request

x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for y in x:
    print(y.decode().strip())

x.close()
