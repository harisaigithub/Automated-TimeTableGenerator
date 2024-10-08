import os

# Use Railway's DATABASE_URL environment variable or default to local PostgreSQL
DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/timetable_db')
