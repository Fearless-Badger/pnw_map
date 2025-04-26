START TRANSACTION;

CREATE DATABASE IF NOT EXISTS map_database;

USE map_database;

CREATE TABLE IF NOT EXISTS students(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(255),
    mname VARCHAR(255),
    lname VARCHAR(255),
    street_address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(31)
);

CREATE TABLE IF NOT EXISTS events(
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    abstract VARCHAR(2047),
    date DATE,
    event_name VARCHAR(255),
    cost INT,
    street_address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(31)
);

CREATE TABLE IF NOT EXISTS registration(
    student_id INT,
    event_id INT,
    PRIMARY KEY (student_id, event_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

COMMIT;
