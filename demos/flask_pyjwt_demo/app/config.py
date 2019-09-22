DB_USER = 'root'
DB_PASSWORD = '12345678'
DB_HOST = 'localhost'
DB_DB = 'flask_jwt'

DEBUG = True
PORT = 3306
HOST = "127.0.0.1"
SECRET_KEY = "my blog"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB