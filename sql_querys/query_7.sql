SELECT grades.grade, students.name, subjects.name
FROM grades
JOIN students ON students.id = grades.student_id
JOIN subjects ON subjects.id = grades.subject_id
WHERE students.group_id = 3
AND subjects.id = 5;
