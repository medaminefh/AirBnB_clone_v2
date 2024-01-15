-- create a database name hbnb_dev_db and a user name hbnb_dev with password hbnb_dev_pwd --
-- grant all privileges on hbnb_dev_db.* to hbnb_dev@localhost identified by 'hbnb_dev_pwd'; --
-- flush privileges; --

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
