from pymongo import MongoClient

__uri = "mongodb+srv://therealsangwoohan:OWFdD1xhYOX05gBf@cluster0.ztbnw.mongodb.net/<dbname>?retryWrites=true&w=majority"
__cluster = MongoClient(__uri)
__db = __cluster["database0"]

deadlines = __db["deadlines"]
events = __db["events"]
