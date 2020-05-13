class Config():
    def __init__(self, cons):
        self.cons = cons

    @property
    def spider_name(self):
        return self.cons.get("spider_name")

    @property
    def mongo_name(self):
        return self.cons.get('save').get("mongo_name")

    @property
    def mongo_collection(self):
        return self.cons.get('save').get('mongo_collection')

    @property
    def db_type(self):
        return self.cons.get("save").get("pipe")

    @property
    def headers(self):
        return self.cons.get("headers")

    @property
    def data(self):
        return self.cons.get("data")

    @property
    def method(self):
        return self.cons.get("method")

    @property
    def params(self):
        return self.cons.get("params")

    @property
    def host(self):
        return self.cons.get("host")

    @property
    def extract_params(self):
        return self.cons.get()
