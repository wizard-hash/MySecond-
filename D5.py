import sqlite3

pr = sqlite3.connect('School.sqlite')
y = pr.cursor()

y.execute('DROP TABLE IF EXISTS students')
y.execute('CREATE TABLE students (name TEXT,sub TEXT ,subcode INTEGER)')
f = int(input('Number of times :'))
x = 1
while x <= f:
  y.execute('INSERT INTO students (name , sub , subcode)  VALUES ( ? , ? , ?)',(input('enter name:'),input('enter subject'),x))
  x+=1
pr.commit()
y.execute('SELECT name,sub,subcode FROM students ORDER BY name')
print('STUDENTS')
for row in y:
 print(row)

pr.close()
