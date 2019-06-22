  create table SubArea(
     SAid int NOT NULL AUTO_INCREMENT Primary key,
     SAName varchar(100) NOT NULL,
     SAManager varchar(50) NOT NULL
     );
 create table area(
     Areaid int NOT NULL Primary key,
     AreaName varchar(50) NOT NULL,
     AreaManager varchar(50) NOT NULL,
     subAreaid int NOT NULL,
     FOREIGN KEY (subAreaid) REFERENCES subarea(SAid)
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
     foreign key (Areacode) references area(Areaid)
     );