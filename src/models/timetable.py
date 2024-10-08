class Timetable:
    def __init__(self):
        self.entries = []

    def is_available(self, teacher, time_slot):
        # Check if the teacher is available during the given time slot
        for entry in self.entries:
            if entry['teacher'] == teacher and entry['time_slot'] == time_slot:
                return False
        return True

    def is_classroom_free(self, class_section, time_slot):
        # Check if the classroom is free during the given time slot
        for entry in self.entries:
            if entry['class_section'] == class_section and entry['time_slot'] == time_slot:
                return False
        return True

    def add_entry(self, class_section, subject, teacher, time_slot):
        self.entries.append({
            'class_section': class_section,
            'subject': subject,
            'teacher': teacher,
            'time_slot': time_slot
        })

    def serialize(self):
        return self.entries
    