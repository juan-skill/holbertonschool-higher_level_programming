-- creates the MySQL server user user_0d_1
-- new user within the MySQL shell
-- provide the user with access to the information they will need
-- you want to set up for your new users, always be sure to reload all the privileges.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
