-- Table: log_in_attempts
CREATE TABLE log_in_attempts (
    id INTEGER PRIMARY KEY,
    login_date DATE,
    login_time TIME,
    success BOOLEAN,
    country TEXT
);

INSERT INTO log_in_attempts (login_date, login_time, success, country) VALUES
('2022-05-08', '19:30', FALSE, 'USA'),
('2022-05-08', '21:00', TRUE, 'MEXICO'),
('2022-05-09', '20:15', FALSE, 'CANADA');

-- Table: employees
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    office TEXT
);

INSERT INTO employees (name, department, office) VALUES
('Alice', 'Marketing', 'East101'),
('Bob', 'Finance', 'West202'),
('Charlie', 'IT', 'Main301');
