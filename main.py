import sqlite3 as sq

cn = sq.connect("database1.sl3")
cur = cn.cursor()
# cur.execute("CREATE TABLE tb1(name TEXT)")
# cur.execute("INSERT INTO tb1 (name) VALUES ('j')")
# cur.execute("INSERT INTO tb1 (name) VALUES ('з')")
# cur.execute("INSERT INTO tb1 (name) VALUES ('5')")

cur.execute("SELECT rowid, name FROM tb1")
cn.commit()

for i in cur.fetchall():
    print(i)

cn.close()
