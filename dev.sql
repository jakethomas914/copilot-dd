-- define a select statement to get all students enrolled in a course

SELECT students.first_name, students.last_name, students.email, students.phone, students.city, students.state, students.zip_code
FROM courses.students
JOIN courses.registrations
ON students.student_id = registrations.student_id
JOIN courses.registration_items
ON registrations.registration_id = registration_items.registration_id
WHERE registration_items.course_id = 1;

-- write an index to improve the performance of the query
CREATE INDEX idx_course_id ON courses.registration_items (course_id);

-- define a table for student attendance to capture attendance by class
CREATE TABLE courses.attendance (
    attendance_id INT IDENTITY (1, 1) PRIMARY KEY,
    registration_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    attendance_status tinyint NOT NULL,
    -- Attendance status: 1 = Present; 2 = Absent; 3 = Late; 4 = Excused
    FOREIGN KEY (registration_id) REFERENCES courses.registrations (registration_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- define a stored procedure to get course enrollment by location
CREATE PROCEDURE GetCourseEnrollmentByLocation
    @CourseID INT,
    @City NVARCHAR(50),
    @State NVARCHAR(50)
AS
BEGIN
    SELECT students.first_name, students.last_name, students.email, students.phone, students.city, students.state, students.zip_code
    FROM courses.students
    JOIN courses.registrations
    ON students.student_id = registrations.student_id
    JOIN courses.registration_items
    ON registrations.registration_id = registration_items.registration_id
    WHERE registration_items.course_id = @CourseID
    AND students.city = @City
    AND students.state = @State;
END;

-- define a stored procedure to get instructor details associated with a location
CREATE PROCEDURE GetInstructorDetailsByLocation
    @InstructorID INT
AS
BEGIN
    SELECT instructors.first_name, instructors.last_name, instructors.email, instructors.phone, 
           locations.city, locations.state, locations.zip_code, 
           courses.course_name, courses.course_description
    FROM courses.instructors
    JOIN courses.instructor_locations
    ON instructors.instructor_id = instructor_locations.instructor_id
    JOIN courses.locations
    ON instructor_locations.location_id = locations.location_id
    JOIN courses.course_instructors
    ON instructors.instructor_id = course_instructors.instructor_id
    JOIN courses.courses
    ON course_instructors.course_id = courses.course_id
    WHERE instructors.instructor_id = @InstructorID;
END;

SELECT * FROM courses.registrations 
WHERE YEAR(registration_date) = 2023 
AND MONTH(registration_date) = 9;