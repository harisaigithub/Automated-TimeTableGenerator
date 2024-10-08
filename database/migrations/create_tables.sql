CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE timetables (
    id SERIAL PRIMARY KEY,
    class_id INT,
    subject VARCHAR(255),
    teacher_id INT,
    time_slot VARCHAR(50)
);
