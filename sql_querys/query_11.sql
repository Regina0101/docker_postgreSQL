SELECT students.name, subjects.name, teachers.name, avg(grades.grade) 
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = 5 AND teachers.id = 2
group by students.name, subjects.name, teachers.name
;
