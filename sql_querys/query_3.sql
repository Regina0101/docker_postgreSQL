SELECT subjects.name AS subject_name, students.group_id, AVG(grades.grade) AS average_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.subject_id = 2
GROUP BY students.group_id, subjects.name;

