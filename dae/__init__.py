from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

__uri = "mongodb+srv://therealsangwoohan:OWFdD1xhYOX05gBf@cluster0.ztbnw.mongodb.net/<dbname>?retryWrites=true&w=majority"
__cluster = MongoClient(__uri)
__db = __cluster["database0"]

deadlines = __db["deadlines"]
events = __db["events"]

deadlines.insert_one({"test": 123})

from dae.views import main
