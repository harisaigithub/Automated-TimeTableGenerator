import unittest
from src.models.class_model import Class  # Assuming your class model is in src/models/class_model.py
from src.models.user import Teacher  # Teacher should be in src/models/user.py
from src.algorithms.timetable_generator import generate_timetable  # Algorithm should be in src/algorithms/timetable_generator.py

class TestTimetableGeneration(unittest.TestCase):
    def test_no_clashes(self):
        # Creating a list of Class objects with subjects
        classes = [Class('Class A', ['Math', 'Science'])]

        # Creating a list of Teacher objects with their availability
        teachers = [Teacher('Mr. Smith', ['Math'], ['9:00-10:00', '10:00-11:00'])]

        # Defining available time slots
        time_slots = ['9:00-10:00', '10:00-11:00']
        
        # Generating the timetable using the algorithm
        timetable = generate_timetable(classes, teachers, time_slots)

        # Ensuring that two entries are made in the timetable (for Math and Science)
        self.assertEqual(len(timetable.entries), 2)

if __name__ == '__main__':
    unittest.main()
