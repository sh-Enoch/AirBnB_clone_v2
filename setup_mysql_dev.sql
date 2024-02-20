-- This script prepares a MySQL server for the AirBnB project

-- Creating the database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creating a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting the priviledge on hbnb_dev_db
GRANT ALL PRIVILEDGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Give select priviledge on performance_schema to hbnb_dev_db
GRANT  SELECT PRIVILEDGES ON performance_schema.* TO 'hbnb_dev_db'@'localhost';
