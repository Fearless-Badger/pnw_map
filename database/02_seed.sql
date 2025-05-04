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
(1, 'Gather your friends and join Intramural Cricket!', '2025-04-27 11:00:00', 'Intramural Cricket', 0, 'Gyte Annex', 'Hammond', 'IN', '46323'),
(2, 'Get ready to tackle the competition in our Fishing Challenge!', '2025-04-28 09:00:00', 'Intramural Fishing Challenge', 0, 'PNW Campus Lake', 'Hammond', 'IN', '46323'),
(3, 'Prepare to expand your global horizons at our Study Away session.', '2025-04-28 12:00:00', 'Study Away 101: Students'' Guide to Going Global', 0, 'Purdue University Northwest Library', 'Hammond', 'IN', '46323'),
(4, 'Take a break from studying and come have some fun with pancakes!', '2025-04-28 12:00:00', 'Pancake Study Break (Westville)', 5, 'Purdue University Northwest - Westville Campus', 'Westville', 'IN', '46391'),
(5, 'Celebrate the College of Humanities, Education, and Social Sciences!', '2025-04-30 13:00:00', 'CHESS Day of Giving Party!', 0, 'CHESS Building Lawn', 'Hammond', 'IN', '46323')
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