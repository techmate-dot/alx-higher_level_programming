# # 0x0D. SQL - Introduction

basic list of commands required to manipulate a database

0. A scripts that show the list of database in your server;
   
   ```sql
   SHOW DATABASES;
   ```

1. A script that creates the database `hbtn_0c_0` in your MySQL server.
   
   ```sql
   CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
   ```

2. A  script that deletes the database `hbtn_0c_0` in your MySQL server.
   
   ```sql
   DROP DATABASE IF EXISTS hbtn_0c_0;
   ```

3. A script that lists all the tables of a database in your MySQL server.
   
   ```sql
   SHOW TABLES IN mysql;
   ```

4. A script that creates a table called `first_table` in the current database in your MySQL server.
   
   ```sql
   CREATE TABLE IF NOT EXISTS first_table(
       id INT,
       name VARCHAR(256)
   );
   ```

5.  prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
   
   ```sql
   SHOW CREATE TABLE first_table;
   ```

6.  lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
   
   ```sql
   SELECT * FROM first_table;
   ```

7. inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
   
   ```sql
   INSERT INTO first_table(id, name) VALUES (89,'Best School');
   ```
   
   8. 


























