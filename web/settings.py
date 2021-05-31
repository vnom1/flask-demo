from os import environ
from dotenv import load_dotenv
load_dotenv() 

SECRET_KEY = environ.get('SECRET_KEY')
DEBUG=environ.get('DEBUG')
TESTING = 0
ENV=environ.get('ENV')
TEST_=environ.get('TEST_')