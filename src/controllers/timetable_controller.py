from flask import Flask, request, jsonify, render_template
from src.services.timetable_service import TimetableService

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
