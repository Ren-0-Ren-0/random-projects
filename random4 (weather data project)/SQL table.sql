CREATE DATABASE weatherDB;

USE weatherDB;

CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    temperature FLOAT,
    weather_description VARCHAR(255)
);
