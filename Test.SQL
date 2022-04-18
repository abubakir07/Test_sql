CREATE DATABASE JORGO_TAXI; 
\с JORGO_TAXI 
CREATE TABLE automoble [ 
    make varchar (20), 
    model varchar (20), 
    fill varchar (20), 
    engine varchar (20),  
    box_peredach varchar (20), 
    years int, 
    color varchar (10) 
]; 
CREATE TABLE voditel [ 
    names varchar (10), 
    surename varchar (40); 
    date_of_bith varchar (20), 
    gender varchar (20) 
]; 
CREATE TABLE operator [ 
    names varchar (10), 
    surename varchar (40); 
    date_of_bith varchar (20), 
    gender varchar (20) 
];

INSERT INTO automoble VALUES ('BMW', 'x5', 'бензин', 'в литрах', 'механика', 2012, 'pink'), ('Mercedes', 's350', 'бензин', 'в литрах', 'автомат', 2012, 'pink'), ('Toyota', 'Camry', 'бензин', 'в литрах', 'автомат', 2012, 'red'), ('BMW', 'x350', 'дизель', 'в литрах', 'механика', 2013, 'pink'), ('Toyota', 'Camry', 'бензин', 'в литрах', 'механика', 2003, 'yellow'), ('BMW', 'x5', 'бензин', 'в литрах', 'механика', 2012, 'pink'), ('Mercedes', 's350', 'электричество', 'в kW для электромобилей', 'автомат', 2022, 'pink'), ('Toyota', 'Camry', 'бензин', 'в литрах', 'автомат', 2012, 'red'), ('BMW', 'x350', 'бензин', 'в литрах', 'механика', 2013, 'pink'), ('Toyota', 'Camry', 'электричество', 'в kW для электромобилей', 'механика', 2020, 'yellow')
INSERT INTO voditel VALUES ('name1','lname1','1999г 15 апреля',10,'male' ),('Азамат','Азаматов','1999г 15 апреля',1,'male' ),('name3','surename3','1999г 15 апреля',5,'female' ,)('name4','surename4','1999г 15 апреля',10,'male' ),('name5','surename5','1999г 15 апреля',15,'female'),('name6','surename6','1999г 15 апреля',24,'male' ),('name7','surename7','1999г 15 апреля',30,'male' ),('name8','surename8','1999г 15 апреля',40,'female' ),('name9','surename9','1999г 15 апреля',1,'male' ),('name10','surename10','1999г 15 апреля',8,'male' );
INSERT INTO operator VALUES('name1','surename','1222year 12 may','male'),('name2','surename2','1222year 12 may','male'),('name3','surename','1222year 12 may','male'),('name4','surename4','1222year 12 may','male'),('name5','surename5','1222year 12 may','male'),('name6','surename6','1222year 12 may','male'),('name7','surename7','1222year 12 may','male'),('name8','surename8','1222year 12 may','male'),('name9','surename9','1222year 12 may','male'),('name10','surename10','1222year 12 may','male');


