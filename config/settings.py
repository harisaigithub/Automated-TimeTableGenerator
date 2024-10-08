import os

DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/timetable_db')
