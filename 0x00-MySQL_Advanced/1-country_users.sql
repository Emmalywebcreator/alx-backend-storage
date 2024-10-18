-- Task: Create a table 'users' with id, email, name, and country attributes
-- The table will have id as primary key, email will be unique,
-- and country will have a default value from an enumeration
-- Ensure the script does not fail if the table already exists
CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM ('US', 'CO', 'TN') NOT NULL
);
