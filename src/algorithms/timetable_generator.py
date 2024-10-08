import random
from models.timetable import Timetable

def generate_timetable(classes, teachers, time_slots):
    """
    Generates a timetable for a set of classes and teachers based on available time slots.
    
    Args:
        classes (list): List of Class objects.
        teachers (list): List of Teacher objects.
        time_slots (list): Available time slots.
    
    Returns:
        Timetable: Generated timetable object.
    """
    timetable = Timetable()
    for cls in classes:
        for subject in cls.subjects:
            allocated = False
            while not allocated:
                time_slot = random.choice(time_slots)
                teacher = random.choice(teachers)
                if timetable.is_available(teacher, time_slot) and timetable.is_classroom_free(cls, time_slot):
                    timetable.add_entry(cls, subject, teacher, time_slot)
                    allocated = True
    return timetable
