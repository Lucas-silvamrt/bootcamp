create database venda;
use venda;
create table pedidos(
codigo int primary key,
nome varchar (100),
valor float);
insert into pedidos (codigo,nome,valor)values
(123,'maça',10.99),
(124,'banana',8.99),
(125,'pera',6.99),
(126,'mamão',7.99);
select * from pedidos;
delete from pedidos where codigo>1;
insert into pedidos (codigo,nome,valor)values
(1,'lápis',2.44),
(2,'caderno',12.50),
(3,'caneta',3.20),
(4,'borracha',0.65),
(5,'caixa',4.39);
select nome,valor from pedidos where valor<20;