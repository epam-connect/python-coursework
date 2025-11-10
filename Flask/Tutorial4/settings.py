import os
db_path = os.path.join('C:\\Ankan Debnath\\Practice\\Python\\Flask\\Tutorial4', 'sample.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
SQLALCHEMY_TRACK_MODIFICATIONS = False