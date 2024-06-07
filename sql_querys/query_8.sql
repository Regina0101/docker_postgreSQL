SELECT teachers.name, subjects.name, AVG(grades.grade) AS grade
FROM subjects
JOIN teachers ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
WHERE teachers.id = 4
GROUP BY teachers.name, subjects.name;
