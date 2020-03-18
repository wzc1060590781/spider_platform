
def get_spider_name(cons):
    return cons.get("spider_name")

def get_mongo_name(cons):
    return cons.get('save').get("mongo_name")

def get_mongo_collection(cons):
    return cons.get('save').get('mongo_collection')

def get_db_type(cons):
    return cons.get("save").get("pipe")
