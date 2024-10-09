function generateTimetable() {
    fetch('/generate_timetable', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "school": {
                "classes": {
                    "Class A": ["Math", "Science"],
                    "Class B": ["History", "English"]
                }
            },
            "constraints": {
                "teachers": ["Mr. Smith", "Mrs. Johnson"],
                "time_slots": ["9:00-10:00", "10:00-11:00"]
            }
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').innerText = 'Timetable generated successfully! Check the view timetable page.';
        console.log(data);
    })
    .catch(error => {
        document.getElementById('message').innerText = 'Error generating timetable!';
        console.error('Error:', error);
    });
}
