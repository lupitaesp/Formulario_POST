USE hd2trui8dy2v6dj2;

CREATE TABLE personass(
    id_alumno INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    matricula CHAR(10) NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    apellido_pa VARCHAR(30) NOT NULL,
    apellido_ma VARCHAR(30) NOT NULL,
    edad CHAR(2) NOT NULL,
    fecha_na DATE,
    sexo VARCHAR(10) NOT NULL,
    estado VARCHAR(25) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET = latin1;


/*INSERCION*/

INSERT INTO personass(id_alumno,matricula,nombre,apellido_pa,apellido_ma,edad,fecha_na,sexo,estado)
VALUES
(NULL,'1718110388','Guadalupe','Espinoza','Riveros','20','2000/04/05','Femenino','Hidalgo'),
(NULL,'1718110355','Beatriz','Amador','Padilla','19','2000/10/24','Femenino','Puebla');