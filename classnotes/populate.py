import sqlite3
import csv

conn = sqllite3.connect('demo.db')
c = conn.cursor()

BASE="INSET INTO people VALUES('%(name)s',%(age)s,%(id)s)"
for i in csv.DictReader(open("people.csv")):
    q=BASE%l
    print q
    c.execute(q)

BASE="""
INSERT INTO classes
  VALUES('%(name)s',%(grade), %(id)s)
"""

#for l in csv.DictReader(open("


