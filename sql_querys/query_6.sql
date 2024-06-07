SELECT groups.id, students.name
FROM groups
JOIN students ON groups.id = students.group_id
WHERE groups.id = 3;
