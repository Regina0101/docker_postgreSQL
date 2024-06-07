SELECT subjects.name, teachers.name
FROM teachers
JOIN subjects ON subjects.teacher_id = teachers.id
WHERE teachers.id = 3;