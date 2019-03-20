import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MONGODB_URI = os.environ.get("MONGODB_URI")
    REDIS_URL = os.environ.get("REDIS_URI")
    SERVER = "0.0.0.0"
    PORT = int(os.environ.get("MONGODB_URI", 3000))
    DEBUG = bool(os.environ.get("DEBUG", True))


    #assert MONGODB_URI ,"MONGODB_URI must be defined"
    @staticmethod
    def init_app(app):
        pass
