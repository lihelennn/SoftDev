import random
from pymango import MongoClient

# connection = Mongoclient('hostname')

connection=MongoClient()
# db = connection.admin
# or connection['admin']
# db.authenticate ('username', 'pw')

db=connection['pd5']

print db.collection_names()

names = ["Thluffy", "Bucky", "Susan", "Victor", "Sarah", "Kictor"]

dtype = ['plain', 'frosted', 'glazed', 'jelly']

for i in range(10):
    d = {"name":random.choice(names),
         "donut"random.chouce(dtype),
         "age":random.randrange(10,30)        
         }
    print d
    db.insert(d)

res = db.people.find({"donut":"plain"})
for r in red:
    print r
