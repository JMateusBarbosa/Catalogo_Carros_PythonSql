create database catalogo_de_carrosV1;
use catalogo_de_carrosV1;


create table login (
	id int primary key not null auto_increment,
    nome varchar(100) not null,
    senha varchar(20) not null
    );


create table Sedãs(
	id int primary key not null auto_increment,
    marca varchar(50) not null,
    nome varchar (50) not null,
    valor varchar (50) not null,
    descrição varchar (2000)
); 
insert into Sedãs(marca , nome, valor,descrição) values ('Caoa Chery','Arrizo 5','R$ 79.490 (RT) a R$ 91.790 (RXS)','Sedã compacto estreou em 2018 
e hoje está disponível em três versões: RT, RTS e RXS. Tem um motor 1.5 turboflex de até 150 cv. A transmissão é do tipo CVT e simula nove marchas.'),
('Chevrolet','Joy Plus','R$ 63.830','O motor é o conhecido 1.0 de quatro cilindros, que entrega até 80 cv com etanol. A única opção de transmissão é
 a manual de seis velocidades.'),
 ('Fiat','Cronos','R$ 71.879 (1.3) a R$ 96.462 (HGT AT)','Vendido em duas motorizações: 1.3 de quatro cilindros e 1.8 16V. O hatch pode ser encomendado 
 com câmbio manual de seis marchas (nas versões com motores 1.3) e automático de seis marchas (apenas nas configurações com motor de 1,8 litro).');
 
 create table Esportivos(
	id int primary key not null auto_increment,
    marca varchar(50) not null,
    nome varchar (50) not null,
    valor varchar (50) not null,
    descrição varchar (2000)
);
 
insert into Esportivos (marca , nome, valor,descrição) values ('Porsche','718 Boxster 2.0 T ','R$ 499.000','2.0 boxer turbo de quatro cilindros, 
300cv , 38,7 kgfm e 0 a 100 km/h em apenas 4,7 s.'),
('BMW','M235i xDrive Gran Coupé  2.0','R$ 390.950','O 2.0 turbo gera 306 cv e 45,9 kgfm, e, em conjunto com o câmbio automático de oito marchas 
e a tração integral.'),
('Mercedes','AMG A 35 2.0 4Matic','R$ 416.900','Motor 2.0 turbo do Mercedes A 35 306 cv e 40,8 kgfm. Com isso, ele é capaz de ir de 0 a
 100 km/h em 4,7 s. O câmbio automatizado tem dupla embreagem e sete marchas e  tração integral.');
 
 create table Caminhonete(
	id int primary key not null auto_increment,
    marca varchar(50) not null,
    nome varchar (50) not null,
    valor varchar (50) not null,
    descrição varchar (2000)
);

insert into Caminhonete (marca , nome, valor,descrição) values ('TOYOTA','HILUX','R$ 220.690 a R$ 354.790','Os motores disponíveis são: o 2.7 flex 
de 4 cilindros, que rende 163 cv e 25 kgfm com etanol e 159 cv e o mesmo torque com gasolina, o 2.8 turbodiesel de 177 cv e 45,9 kgfm, 
e o V6 4.0 de 234 cv e 38,3 kgfm.'), 
('FORD','F-150 Raptor','R$ 500.000 a R$ 900.000','V6 EcoBoost 3.5 Biturbo, 456 cv, 78,7 kgfm com transmição 
Automática de 10 marchas.'),
('RAM','RAM 2500 Laramie','R$ 459.000 a R$ 600.000','Motor 6.7 Cummins, Tipo Dianteiro, Longitudinal e Turbodiesel, 6 cilidros em linha, 365 cv a 2.800 rpm,
Troque 110,6 kgfm a 1.600 rpm.')
;
