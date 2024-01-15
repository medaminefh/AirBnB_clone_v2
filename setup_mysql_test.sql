-- create a database name hbnb_dev_db and a user name hbnb_dev with password hbnb_dev_pwd if they're not exist
-- grant all privileges on hbnb_dev_db.* to hbnb_dev@localhost identified by 'hbnb_dev_pwd'
-- flush privileges

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;