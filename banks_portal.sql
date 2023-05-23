create database banks_portal;
use banks_portal; 
create table accounts (
accountId int not null unique auto_increment,
ownerName varchar(45) not null,
owner_ssn int not null,
balance decimal (10,2) default 0.00,
account_status varchar (45), 
primary key (accountId)
);

select * from accounts;


create table if not exists transactions (
transactionId int not null unique auto_increment, 
accountId int not null,
transactionType varchar(45) not null,
transactionAmount decimal (10,2) not null,
primary key (transactionId)
);

select * from transactions;

use banks_portal; 

insert into accounts (ownerName, owner_ssn, balance, account_status)
values("Maria Jozef", 123456789, 10000.00, "active"), 
("Linda Jones", 987654321, 2600.00, "inactive"), 
("John McGrail", 222222222, 100.50, "active"),
("Patty Luna", 111111111, 509.75, "inactive");

select * from accounts;

insert into transactions (accountId, transactionType, transactionAmount) 
values(1, "deposit", 650.98), 
(3, "withdraw", 899.87), 
(3, "deposit", 350.00);

select * from transactions; 

use banks_portal;
delimiter //
create procedure accountTransactions(in accountId int)
begin
select * from transactions where transactionId = accountId;
 end;
 
 delimiter //
 create procedure deposit ( in accoundID int, in amount decimal (10,2))
 begin
 insert into transactions (accountId, transactionType, transactionAmount)
 values (accountID, "deposit", amount);
 update accounts set balance = balance + amount where accoundID=accountID;
 end; 
 
 delimiter //
 create procedure withdraw ( in accoundID int, in amount decimal (10,2))
 begin
 insert into transactions (accountId, transactionType, transactionAmount)
 values (accountID, "withdraw", amount);
 update accounts set balance = balance + amount where accoundID=accountID;
 end; 
 
 
 
 
 
 
 
 
 