import random
from src.models.timetable import Timetable

def generate_timetable(classes, teachers, time_slots):
    timetable = Timetable()
    
    for class_section, subjects in classes.items():
        for subject in subjects:
            allocated = False
            while not allocated:
                time_slot = random.choice(time_slots)
                teacher = random.choice(teachers)
                
                if timetable.is_available(teacher, time_slot) and timetable.is_classroom_free(class_section, time_slot):
                    timetable.add_entry(class_section, subject, teacher, time_slot)
                    allocated = True
    
    return timetable
