-- prepares mysql server for the project
-- creates database new user and grants privileges

CREATE DATABASE IF NOT EXISTS  hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hnbn_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
