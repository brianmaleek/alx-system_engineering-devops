-- SQL script to create a user and password for the database
-- Grants replication privileges to the user
-- Create a user and password for the database
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
