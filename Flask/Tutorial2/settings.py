class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///flask.db'

class Prod(Config):
    DATABASE_URI = '<db_connection_string>'

class Dev(Config):
    DEBUG = True

class Test(Config):
    TESTING = True