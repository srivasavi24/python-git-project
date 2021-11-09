#mongodb in python
from pymongo import MongoClient

client=MongoClient('127.0.0.1',27017)
db=client['kits']
c=db['ml']


for i in c.find():
   print(i)

