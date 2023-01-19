CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;
-- vamos a crear 2 tablas
CREATE TABLE IF NOT EXISTS usuarios(
id int(25) auto_increment not null,-- no tiene q haber null en esta columna
nombre varchar(100),
apellidos varchar(255),
email varchar(255) not null,
password varchar(255) not null,
fecha date not null,
constraint pk_ususarios primary key (id),  -- restricciones de la tabla
constraint uq_email UNIQUE (email) -- restricccion de campo unico para que no se repita el mail 
 )ENGINE=InnoDb;-- esto significa que va a mantener la integridad referencial y relaciones entre tablas 

create table if not EXISTS notas(
id int(25) auto_increment not null,
usuario_id int(25) not null,
titulo varchar(255) not null,
descripcion mediumtext,
fecha date not null,
constraint pk_notas primary key (id),
constraint fk_notas foreign key (usuario_id) references usuarios(id) -- relaciona el campo ususario id con la tabla usuario y dentro de usuario id guardo los registros de id de la otra tabla
)ENGINE=InnoDb;