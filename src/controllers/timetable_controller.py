from flask import Blueprint, request, jsonify, render_template
from src.services.timetable_service import TimetableService
import os

# Create a blueprint
timetable_app = Blueprint('timetable_app', __name__, template_folder=os.path.abspath('web/templates'))

# Routes
@timetable_app.route('/')
def index():
    return render_template('index.html')

@timetable_app.route('/generate_timetable', methods=['POST'])
def generate_timetable():
    data = request.get_json()
    school = data.get('school', {})
    constraints = data.get('constraints', {})

    timetable_service = TimetableService()
    timetable = timetable_service.create_timetable(school, constraints)

    return jsonify(timetable.serialize())
