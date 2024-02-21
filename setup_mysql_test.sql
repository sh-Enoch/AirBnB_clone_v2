#!/bin/bash

# MySQL credentials
MYSQL_USER="root"
MYSQL_PASSWORD="bsitc01/"

# Database and user information
DATABASE="hbnb_test_db"
USER="hbnb_test"
PASSWORD="hbnb_test_pwd"

# Create database if not exists
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS $DATABASE;"

# Create user if not exists
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE USER IF NOT EXISTS '$USER'@'localhost' IDENTIFIED BY '$PASSWORD';"

# Grant privileges on hbnb_test_db
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "GRANT ALL PRIVILEGES ON $DATABASE.* TO '$USER'@'localhost';"

# Grant SELECT privilege on performance_schema
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "GRANT SELECT ON performance_schema.* TO '$USER'@'localhost';"
