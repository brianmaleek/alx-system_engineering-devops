-- SQL script to create a user and password for the database
-- Grants replication privileges to the user
-- Create a user and password for the database
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'password01';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

-- Show grants for 'replica_user'@'%'
SHOW GRANTS FOR 'replica_user'@'%';

-- Show grants for 'holberton_user'@'localhost'
SHOW GRANTS FOR 'holberton_user'@'localhost';
