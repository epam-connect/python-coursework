from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, DATE
from sqlalchemy_utils import PasswordType

from ..database import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(length=150))
    last_name = Column(String(length=150))
    email = Column(String(length=255), unique=True)
    DOB = Column(DATE, nullable=True)
    password = Column(PasswordType(
        schemes= ['pbkdf2_sha512', 'md5_crypt'],
        deprecated=['md5_crypt']
    ))
