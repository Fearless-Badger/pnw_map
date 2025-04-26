START TRANSACTION;

USE map_database;

INSERT INTO students (student_id, fname, mname, lname, street_address, city, state, zip_code)
VALUES
(1, 'Micah', 'H', 'Najacht', '123 Main St', 'Hammond', 'IN', '46323'),
(2, 'John', 'A', 'Doe', '9632 N Cline Ave', 'Highland', 'IN', '46322')
ON DUPLICATE KEY UPDATE
fname = VALUES(fname),
mname = VALUES(mname),
lname = VALUES(lname),
street_address = VALUES(street_address),
city = VALUES(city),
state = VALUES(state),
zip_code = VALUES(zip_code);


INSERT INTO events (event_id, abstract, date, event_name, cost, street_address, city, state, zip_code)
VALUES
(1, 'A fun student event', '2025-05-01', 'Student Life Fair', 0, '2200 169th St', 'Hammond', 'IN', '46323'),
(2, 'A networking event for students', '2025-06-15', 'Career Networking Night', 10, '2233 173rd St', 'Hammond', 'IN', '46323')
ON DUPLICATE KEY UPDATE
abstract = VALUES(abstract),
date = VALUES(date),
event_name = VALUES(event_name),
cost = VALUES(cost),
street_address = VALUES(street_address),
city = VALUES(city),
state = VALUES(state),
zip_code = VALUES(zip_code);

INSERT INTO registration (student_id, event_id)
VALUES
(1, 1),
(2, 2)
ON DUPLICATE KEY UPDATE
student_id = VALUES(student_id),
event_id = VALUES(event_id);

COMMIT;