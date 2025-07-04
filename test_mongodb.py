from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError
import ssl

uri = "mongodb+srv://PradeepKumar:pradeep531@cluster0.dz9f9k8.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=False, serverSelectionTimeoutMS=10000)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except (ConnectionFailure, ConfigurationError, Exception) as e:
    print("Connection failed:", e)
