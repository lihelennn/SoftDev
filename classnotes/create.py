# % is a placeholder
# python string subs


import sqlite3

conn = sqlite3.connect("demo.db")

c = conn.cursor

q = "create table people (name text, age integer, id integer)"
c.execute(q)


#create a string with sql command --> give to cursor

q = "create table classes(name text, grade integer, id integer)"
c.execute(q)

conn.commit()
