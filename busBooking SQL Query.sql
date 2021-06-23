CREATE DATABASE BusBooking;

CREATE TABLE u_profile(uid INT PRIMARY KEY AUTO_INCREMENT , u_name VARCHAR (30) UNIQUE , PASSWORD VARCHAR(30),
mobile VARCHAR (20) UNIQUE , age INT,role VARCHAR (30));

CREATE TABLE route(rid INT PRIMARY KEY AUTO_INCREMENT , r_name VARCHAR (30) UNIQUE );

CREATE TABLE bus(bid INT PRIMARY KEY AUTO_INCREMENT , b_name VARCHAR(30) UNIQUE ,route_id INT , FOREIGN KEY (route_id)
 REFERENCES route(rid));

CREATE TABLE pnr(pid INT PRIMARY KEY AUTO_INCREMENT , user_id INT , bus_name VARCHAR(30), no_of_seats INT ,journey_date VARCHAR(30) ,
amount INT ,FOREIGN KEY (user_id) REFERENCES u_profile (uid),FOREIGN KEY (bus_name) REFERENCES bus (b_name));

