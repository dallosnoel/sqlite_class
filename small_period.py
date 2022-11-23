import sqlite3

con = sqlite3.connect("peri.db")

cur = con.cursor()

class Peri:
    def __init__ (self, sor):
        rendszam, nev, jel, *felesleg = sor.strip().split(",")
        self.rendszam = rendszam
        self.nev = nev
        self.jel = jel

with open("peritable.csv", encoding = "latin2") as f:
    elso_sor = f.readline()
    data = [Peri(sor) for sor in f]
    
cur.execute("DROP TABLE IF EXISTS perta")
cur.execute("CREATE TABLE perta(rendszam, nev, jel)")

for i in data:
    adat = [(i.rendszam, i.nev, i.jel)]
    cur.executemany("INSERT INTO perta VALUES(?, ?, ?)", adat)

con.commit()

msg = cur.execute("SELECT * FROM perta")

#print(msg.fetchall())

for row in cur.execute("SELECT rendszam, nev, jel FROM perta"):
    print(f"Rendszám: {row[0]}, Név: {row[1]}, Jel: {row[2]}")









