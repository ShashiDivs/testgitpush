import pymongo
client = pymongo.MongoClient("mongodb+srv://sasidivs:sasiMongo09@cluster0.vn9g8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

