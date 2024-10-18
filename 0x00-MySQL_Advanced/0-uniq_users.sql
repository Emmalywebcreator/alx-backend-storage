-- Task: Create a table 'users' with id, email, and name attributes
-- The table will have id as primary key, email will be unique
-- Ensure the script does not fail if the table already exists

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
);
