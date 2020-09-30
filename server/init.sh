#!/bin/bash

TEMP_FILE='/var/tmp/mysql-user.sql'
cat > "$TEMP_FILE" << EOF
ALTER USER 'root'@'localhost' IDENTIFIED BY 'some_pass';
CREATE USER 'redes'@'%' IDENTIFIED BY 'some_pass';
GRANT ALL PRIVILEGES ON *.* TO 'redes'@'%';
ALTER USER 'redes'@'%' IDENTIFIED WITH mysql_native_password BY 'some_pass';
EOF
