  CREATE database safety;
  use safety;
 create table area(
     Areaid int NOT NULL AUTO_INCREMENT Primary key,
     AreaName varchar(50) NOT NULL,
     AreaManager varchar(50) NOT NULL,
     );
  create table SubArea(
     SAid int NOT NULL Primary key,
     Areaid int NOT NULL,
     SAName varchar(100) NOT NULL,
     SAManager varchar(50) NOT NULL,
     FOREIGN KEY (Areaid) REFERENCES area(Areaid)
     );

 create table Readings(
     Rid int NOT null auto_increment primary key,
     Areacode int not null,
     H2S_lvl float,
     N2_lvl float,
     CO_lvl float,
     Cl2_lvl float,
     Pressure_lvl float,
     Smoke bool,
     Timestamp timestamp,
     foreign key (Areacode) references subarea(SAid)
     );
