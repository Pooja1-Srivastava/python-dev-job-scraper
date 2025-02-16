from pymongo import MongoClient

def store_jobs(job_listings):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['job_database']
    collection = db['job_listings']
    
    collection.insert_many(job_listings)