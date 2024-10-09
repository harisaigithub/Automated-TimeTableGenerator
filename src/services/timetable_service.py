from src.algorithms.timetable_generator import generate_timetable

class TimetableService:
    def create_timetable(self, school, constraints):
        classes = school.get('classes', {})
        teachers = constraints.get('teachers', [])
        time_slots = constraints.get('time_slots', [])
        
        if not classes or not teachers or not time_slots:
            raise ValueError("Missing required data: classes, teachers, or time slots")
        
        generated_timetable = generate_timetable(classes, teachers, time_slots)
        self.save_to_db(generated_timetable)  # Placeholder for saving to DB
        return generated_timetable

    def save_to_db(self, timetable):
        # Logic to save the timetable to the database (optional)
        pass
