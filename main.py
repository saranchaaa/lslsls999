import sqlite3 as sq

cn = sq.connect("database1.sl3")
cur = cn.cursor()
# cur.execute("CREATE TABLE tb1(name TEXT)")
cur.execute("INSERT INTO tb1 (name) VALUES ('j')")
cur.execute("INSERT INTO tb1 (name) VALUES ('з')")
cur.execute("INSERT INTO tb1 (name) VALUES ('5')")
cn.commit()

print(cur)
print(cn)

cn.close()
