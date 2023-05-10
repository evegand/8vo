CREATE DATABASE empleados;

USE empleados;

CREATE TABLE datos_empleados (
  id INT NOT NULL,
  nombre VARCHAR(50) NOT NULL,
  apellido_paterno VARCHAR(50) NOT NULL,
  apellido_materno VARCHAR(50),
  puesto VARCHAR(50),
  empresa VARCHAR(50) NOT NULL,
  calle VARCHAR(50),
  numero_exterior VARCHAR(10),
  numero_interior VARCHAR(10),
  colonia VARCHAR(50),
  ciudad VARCHAR(50) NOT NULL,
  estado VARCHAR(50) NOT NULL,
  codigo_postal VARCHAR(10) NOT NULL,
  telefono VARCHAR(20),
  email VARCHAR(100) NOT NULL,
  fecha_nacimiento DATE,
  PRIMARY KEY (id)
);

INSERT INTO datos_empleados (id, nombre, apellido_paterno, apellido_materno, puesto, empresa, calle, numero_exterior, numero_interior, colonia, ciudad, estado, codigo_postal, telefono, email, fecha_nacimiento) VALUES 
(1,'José Luis','González','García','Director General','ABC Company','Calle del Sol','12','4','Colonia del Valle','Monterrey','Nuevo León','64890','55 5555 5555','jlgonzalez@abccompany.com','1970-01-01'), 
(2,'Sofía','Ramírez','Hernández','Coordinadora de Marketing','XYZ Corp','Calle del Roble','105','','Colonia Anzures','Ciudad de México','Ciudad de México','11590','55 1234 5678','sofia.ramirez@xyzcorp.com','1985-02-15'), 
(3,'José Eduardo','García','Rodríguez','Desarrollador de Software','Software SA de CV','Calle del Águila','45','1','Colonia Lomas de Chapultepec','Ciudad de México','Ciudad de México','11000','55 9876 5432','jose.garcia@softwaresa.com','1990-11-30'), 
(4,'María','Pérez','Martínez','Analista de Datos','Data Inc','Calle del Olivo','29','','Colonia San Ángel','Guadalajara','Jalisco','45010','33 3333 3333','mariaperez@datainc.com','1988-05-10'), 
(5,'Francisco','López','Juárez','Ingeniero de Procesos','Procesos SA de CV','Calle del Laurel','17','7','Colonia del Carmen','Ciudad de México','Ciudad de México','04100','55 4444 4444','flopez@procesos.com','1978-09-22'), 
(6,'Martín','Hernández','Sánchez','Asistente de Gerencia','ABC Company','Calle del Bosque','32','','Colonia Santa Fe','Ciudad de México','Ciudad de México','01210','55 6789 0123','mhernandez@abccompany.com','1989-12-12'), 
(7,'Ana Karen','González','Flores','Diseñadora Gráfica','Design Agency','Calle del Pino','76','','Colonia del Valle','Monterrey','Nuevo León','64890','81 2345 6789','akgonzalez@designagency.com','1995-07-07'), 
(8,'Luis Miguel','Torres','Rodríguez','Abogado Corporativo','Legal Firm','Calle del Roble','105','3','Colonia Anzures','Ciudad de México','Ciudad de México','11590','55 6789 0123','lm.torres@legalfirm.com','1976-03-20'),
(9,'María Fernanda','Gómez','Hernández','Ejecutiva de Cuentas','Advertising Agency','Calle del Zafiro','22','','Colonia Polanco','Ciudad de México','Ciudad de México','11560','55 4321 9876','fernanda.gomez@advertisingagency.com','1992-05-11'),
(10,'Juan Carlos','Aguilar','Castillo','Ingeniero de Ventas','Ventas SA de CV','Calle del Sol','44','12','Colonia Las Águilas','Guadalajara','Jalisco','45040','33 2222 2222','jcaguilar@ventassa.com','1983-09-18'),
(11,'Luis','García','Fernández','Director de Marketing','ABC Company','Calle del Sol','123','','Centro','Ciudad de México','Ciudad de México','06000','555-123-4567','luis.garcia@email.com','1985-12-03'),
(12,'Ana','Jiménez','Martínez','Asistente Administrativo','XYZ Corp.','Avenida Juárez','456','302','Reforma','Ciudad Juárez','Chihuahua','32000','656-234-5678','ana.jimenez@email.com','1990-06-15'),
(13,'Carlos','Ortega','Rodríguez','Desarrollador de Software','Acme Inc.','Calle Libertad','789','','La Estrella','Monterrey','Nuevo León','64000','818-345-6789','carlos.ortega@email.com','1995-09-20'),
(14,'Isabel','González','Ramírez','Coordinadora de Ventas','Global Solutions','Calzada de Tlalpan','1010','','Portales Sur','Ciudad de México','Ciudad de México','03300','555-987-6543','isabel.gonzalez@email.com','1987-03-11'),
(15,'Jorge','Rodríguez','Pérez','Analista de Datos','DataMind SA de CV','Av. Revolución','2468','1201','Tlacopac','San Ángel','Ciudad de México','','555-555-1212','jorge.rodriguez@email.com','1992-01-30');

