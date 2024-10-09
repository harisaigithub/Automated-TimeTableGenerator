CREATE TABLE timetable (
    id SERIAL PRIMARY KEY,
    class_section VARCHAR(100),
    subject VARCHAR(100),
    teacher VARCHAR(100),
    time_slot VARCHAR(50)
);
