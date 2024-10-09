from flask import Flask
from src.controllers.timetable_controller import timetable_app  # Import the blueprint

# Initialize Flask app and define static/template folders
app = Flask(__name__, static_folder='web/static', template_folder='web/templates')

# Register the blueprint
app.register_blueprint(timetable_app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
