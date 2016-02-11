import sqlite3

conn = sqlite2.connect("demo.db")

c = conn.cursor()

q = """
   SELECT people.name,classes.name,grade
"""
