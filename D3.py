import sqlite3
x = sqlite3.connect('me.sqlite')
y = x.cursor()
y.execute('DROP TABLE IF EXISTS Tracks')
y.execute('CREATE TABLE Tracks (title TEXT , plays INTEGER)')
y.execute('INSERT INTO Tracks (title ,plays) VALUES (?,?)',(input('enter yitlr :'),54))
x.commit()

print('Tracks:')
y.execute('SELECT title,plays FROM Tracks')
for t in y:
 print(t)
y.execute('DELETE FROM Tracks WHERE plays < 100')
x.commit()
x.close()
