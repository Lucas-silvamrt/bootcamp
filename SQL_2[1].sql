create database suporte;
use suporte;
create table serviço(
	codigo int primary key,
	descricao varchar(100),
	valorunit float not null,
	tempo int);
insert into serviço (codigo,valorunit)values
(6,0),
(7,0),
(8,0),
(9,0),
(10,0),
(11,0),
(12,0),
(13,0),
(14,0),
(15,0),
(16,0);

create table item(
	Nr int primary key,
    codigo int not null,
    num int not null,
	constraint foreign key (codigo) references serviço(codigo) on delete cascade,
    constraint foreign key (num) references pedidos(num) on delete cascade,
    nome varchar(100),
	desconto float,
	valor float);
insert into item(nr,codigo, num,nome,desconto,valor)values
(123,6,33,'maça',12,10.99),
(124,7,334,'banana',10,8.99),
(125,8,335,'pera',8,6.99),
(126,9,336,'mamão',7,7.99),
(1,10,337,'lápis',3,2.44),
(2,11,338,'caderno',0,12.50),
(3,12,339,'caneta',1,3.20),
(4,13,340,'borracha',3,0.65),
(5,14,341,'caixa',4,4.39);
    
create table pedidos(
	num int primary key,
	dt date,
	atendido boolean default false,
	obs varchar (100));
insert into pedidos (num,atendido,obs) values
(33,false,'bom'),
(334,false,'bom'),
(335,false,'bom'),
(336,false,'bom'),
(337,false,'bom'),
(338,false,'bom'),
(339,false,'bom'),
(340,false,'bom'),
(341,false,'bom');

create table cliente(
	cod int primary key,
	nome varchar(100),
	fone int,
	endereco varchar (100),
	email varchar(100));
insert into cliente (cod,nome,fone,endereco,email) values
(132,'lucas',1213138219,'ceub','sdhjakdhgskajhd');
select nome,codigo,num,valor from item where valor<9 order by nome;
select distinct num from pedidos;
select nr from item inner join pedidos on(nr=num);
delete from pedidos where num >1;
