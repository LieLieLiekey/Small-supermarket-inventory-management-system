# Py文件分下面几个 

1. supermarketmanage.py ，负责软件的开始界面和调用其他几个人员界面
2. basic.py ，负责软件与数据库交流的函数，提供软件与数据库所需的基本查询、修改、删除等功能
3. frontdesk.py ，售货员的前台界面以及功能
4. purchasemanage.py ，进货员的前台界面以及功能
5. adminmanage.py  ，管理员的前台界面以及功能
6. generaloperat.py ，包含所有员工共有的一些操作函数
7. commodity.py  ，商品对象的定义
8. cashier.py ，售货员对象的定义
9. purchaser.py ，进货员的定义
10. admin.py 包含管理员对象的定义

注：该代码是sql课程设计，使用python3.7编写前台和后台与数据库交互的部分（from  NYIST 计工学院计科专业 17级DCH） ，费时四天。
其中使用pymssql库进行与数据库的交互.


**运行程序时，只需将这些py放在放在同一目录，只需运行supermarketmanage.py文件,并且需要将sql server中的sa用户，密码改为123（或者自己在supermarmanage.py文件中将init函数内密码修改一下即可）**

**引用的外部包有prettytable、pymssql**
