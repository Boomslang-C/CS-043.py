from lesson06.database import Simpledb

db = Simpledb('db.txt')

text = db.delete('Joey')

print(text)
