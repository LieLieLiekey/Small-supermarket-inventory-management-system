create database Supermarket
use Supermarket
create table Commodity(
commodity_no varchar(10) primary key,/*商品编号*/
commodity__name varchar(20),/*商品名称*/
commodity__type1 varchar(10),/*商品类型*/
commodity__size varchar(5),/*商品规格*/
commodity__sprice float,/*售价*/
commodity__mdate datetime,/*生产日期*/
commodity__edate datetime,/*保质期*/
commodity__quantity int,/*库存数量*/
)

insert into Commodity values('0000000001','奶香曲奇饼干','饼干','袋',7,'2018-12-23 00:00:00.000','2019-02-04 00:00:00.000,150')

go
CREATE TABLE Cashier(
cashier_no varchar(10) primary key,/*员工编号*/
cashier_name varchar(10),
cashier_pwd varchar(10),
cashier_sex char(2),
cashier_age int,
cashier_hourse float,
cashier_salary float,
cashier_phone varchar(11),
)


insert into Commodity values('000004','小王','12345678','男',14,'2019 02 03','2019 03 04',10)
insert into Commodity values('000005','小红','12345678','女',20.0,'2019 02 10','2019 03 10',100)

go 
create table Purchaser(
purchaser_no varchar(10) primary key,/*员工编号*/
purchaser_name varchar(10),
purchaser_sex char(2),
purchaser_age int,
purchaser_salary float,
purchaser_phone varchar(11),
purchaser_entrytime datetime,
)

go
create table Stock(
purchaser_no varchar(10),
commodity_no varchar(10),
stock_no varchar(8),
stock_sprice float,
stock_quantity int,
stock_date datetime,
primary key(stock_no),
foreign key(purchaser_no ) references purchaser(purchaser_no ) on delete set null,
foreign key(commodity_no ) references commodity(commodity_no ) on delete set null,
)
go
create table Sell(
cashier_no varchar(10),
commodity_no varchar(10),
sell_no varchar(8),
sell_quantity int,
sell_price float,/*应收金额*/
sell_rmoney float,/*实收金额*/
sell_date datetime,
primary key(sell_no),
foreign key(cashier_no ) references cashier(cashier_no ) on delete set null,
foreign key(commodity_no ) references commodity(commodity_no ) on delete set null,
)


create table Administrator(
admin_no varchar(10),
admin_pwd varchar(10),
admin_name varchar(10),
admin_phone varchar(10),
admin_addres nvarchar(20),
primary key (admin_no)
)


insert into Administrator values('001','123456','楼下小黑','110','北京市海淀区大同路6号')

insert into Administrator values('dch','123456','隔壁老王','110','北京市海淀区大同路5号')


/*Sell表级联删除触发器*/
CREATE TRIGGER Delete_sellcommodity
ON Commodity
FOR DELETE
AS
DELETE Sell
FROM deleted
WHERE Sell.commodity_no=deleted.commodity_no

/*Sell表级联删除触发器*/
CREATE TRIGGER Delete_sellcashier
ON Cashier
FOR DELETE
AS
DELETE Sell
FROM deleted
WHERE Sell.cashier_no=deleted.cashier_no


/*Stock表级联删除触发器*/
CREATE TRIGGER Delete_stockCommodity
ON Commodity
FOR DELETE
AS
DELETE Stock
FROM deleted
WHERE Stock.commodity_no=deleted.commodity_no


/*Stock表级联删除触发器*/
CREATE TRIGGER Delete_stockpurchaser
ON Purchaser
FOR DELETE
AS
DELETE Stock
FROM deleted
WHERE Stock.purchaser_no=deleted.purchaser_no
