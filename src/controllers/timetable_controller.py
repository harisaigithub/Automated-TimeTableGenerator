from flask import Flask, request, jsonify
from src.services.timetable_service import TimetableService

app = Flask(__name__)

@app.route('/generate_timetable', methods=['POST'])
def generate_timetable():
    data = request.json
    school = data['school']
    constraints = data['constraints']
    timetable = TimetableService().create_timetable(school, constraints)
    return jsonify(timetable.serialize())

if __name__ == '__main__':
    app.run(debug=True)
