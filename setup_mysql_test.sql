-- Create the hbnb_test_db if it doesn't exist
-- create user hbnb_test with pwd hbnb_test_pwd if it doesn't exist
-- grants all privilege on hbnb_test_db and select priv on performance_schema to user

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'
