from flask import Flask, request, jsonify, render_template
from src.services.timetable_service import TimetableService
import os

template_dir = os.path.abspath('web/templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_timetable', methods=['POST'])
def generate_timetable():
    data = request.get_json()
    school = data.get('school', {})
    constraints = data.get('constraints', {})

    timetable_service = TimetableService()
    timetable = timetable_service.create_timetable(school, constraints)

    return jsonify(timetable.serialize())
