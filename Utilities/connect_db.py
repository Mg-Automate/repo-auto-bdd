from pymongo import MongoClient


client = MongoClient("mongodb+srv://SaaRthiConnecTor:PfLsjTcRnOYNZXvK@stagingcluster.nlsde.mongodb.net/saarthiDb")
print("Connection Successful")
client.close()