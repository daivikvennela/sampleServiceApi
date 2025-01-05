APP = OS + application dependencies[python, requirements.txt] + APP code
# Basic Setup 
- CREATE a requirements.txt file 
- CREATE a main.py file 
- CREATE a virtual environment
- python -m venv venv
- ACTIVATE ENV: source venv/bin/activate
- pip install -r requirements.txt
- CREATE main: on vs code 
- filename: app
- UVICORN: uvicorn main:app --reload \
- remote on the same
other network option: uvicorn main:app --reload --host 0.0.0.0  

----

# CRUD w/ MySQL database
- list users 
- add new users
- update exsistiing users
- delete user
----
- add [mysql-connector-python] to reqs
- install dependencies

---
Installing MySQL dockerimage
- docker pull mysql:latest

how to run:
- docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=MySQLPass -p 3306:3306 -d mysql:latest

connect 
- docker exec -it mysql-container mysql -u root -p

### Creating database and empty table 
CREATE DATABASE mySampleDB;
USE mySampleDB;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);









