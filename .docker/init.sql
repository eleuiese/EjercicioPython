CREATE DATABASE IF NOT EXISTS db;
USE db;
CREATE TABLE Datos (id int NOT NULL AUTO_INCREMENT,Cedula int(11),Nombres varchar(255),Direccion varchar(255),latitude DECIMAL(10,6),longitude DECIMAL(10,6),city varchar(255),description varchar(255),PRIMARY KEY (id) ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
