import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/mydatabase')
SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
