-- Create the hbnb_dev_db if it doesn't exist
-- create user hbnb_dev with pwd hbnb_dev_pwd if it doesn't exist
-- grants all privilege on hbnb_dev_db and select priv on performance_schema to user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'
