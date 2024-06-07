SELECT students.name, subjects.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.group_id = 1 AND subjects.id = 4
ORDER BY grades.grade_date DESC;