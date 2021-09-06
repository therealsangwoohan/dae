from pymongo import MongoClient

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

__cluster = MongoClient(os.getenv("URI"))
__db = __cluster["database0"]

deadlines = __db["deadlines"]
events = __db["events"]
