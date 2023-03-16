-- a script that creates a table second-table in the database hbtn_0c_0 in your MySQL server
-- database name will be passed as an argument to the mysql command
-- if the table second_table already exists, your script should not fail

CREATE TABLE IF NOT EXISTS second_table
(
 id INT,
 name VARCHAR(256),
 score INT
);
INSERT INTO second_table
VALUES (1, "John", 10), 
       (2, "Alex", 3), 
       (3, "Bob", 14),
       (4, "George", 8);
