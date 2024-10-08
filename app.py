from src.controllers.timetable_controller import app
import os  # Import os to access environment variables

if __name__ == '__main__':
    # Use the port provided by Railway or default to 5000 locally
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
