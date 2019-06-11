import generaloperat
from basic import Basic
from commodity import Commodity
from purchaser import Purchaser
from admin import Admin
import os
class AdminManage:
    def __init__(self):
        self.admin=None
    def login(self):
        '''前台的登陆'''
        admin_no = input("请输入您的管理员账号:").strip()
        adm = Basic.queryOneAdmin(admin_no)
        if adm==[]:
            print("不存在该账号.")
            return False
        admin = Admin(adm)
        in_pwd = input("请输入您的密码:").strip()
        if admin.getPwd() == in_pwd:
            self.admin = admin
            print("登陆成功.")
            return True
        else:
            print("密码错误.")
            return False
    def metaQuery(self):
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: 查看所有商品信息")
            print("2: 查看所有售货员信息")
            print("3: 查看所有进货员信息")
            print("4: 查看所有售货信息")
            print("5: 查看所有进货信息")
            print("6: 查看单个售货员信息(未开发)")
            print("7: 查看单个进货员信息(未开发)")
            print("8: 查看单个商品信息(未开发)")
            print("                                     其他数字退出")
            print("------------------------------------------------")
            cmd = input("请输入选项:").strip()
            if cmd=="1":
                self.queryAllCommodity()
            elif cmd=="2":
                self.queryAllCashier()
            elif cmd=="3":
                self.queryAllPurchaser()
            elif cmd=="4":
                self.queryAllSell()
            elif cmd=="5":
                self.queryAllStock()
            else:
                break
            os.system("pause")
    def metaAdd(self):
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: 增加新的售货员")
            print("2: 增加新的进货员")
            print("3: 增加新的商品")
            print("                                     其他数字退出")
            print("------------------------------------------------")
            cmd = input("请输入选项:").strip()
            if cmd=="1":
                self.addOneCashier()
            elif cmd=="2":
                self.addOnePurchaser()
            elif cmd=="3":
                self.addOneCommodity()
            else:
                break
            os.system("pause")
    def metaDel(self):
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: 移除一个售货员")
            print("2: 移除一个进货员")
            print("3: 移除一个商品")
            print("                                     其他数字退出")
            print("------------------------------------------------")
            cmd = input("请输入选项:").strip()
            if cmd=="1":
                self.delOneCashier()
            elif cmd=="2":
                self.delOnePurchaser()
            elif cmd=="3":
                self.delOneCommodity()
            else:
                break
            os.system("pause")
    def metaModity(self):
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: 修改售货员信息")
            print("2: 修改进货员信息")
            print("3: 修改库存中商品信息")
            print("                                     其他数字退出")
            print("------------------------------------------------")
            cmd = input("请输入选项:").strip()
            if cmd=="1":
                self.modifyOneCashier()
            elif cmd=="2":
                self.modifyOnePurchaser()
            elif cmd=="3":
                self.modifyOneCommodity()
            else:
                break
            os.system("pause")
    def meta(self):
        '''前台 菜单'''
        if not self.login():
            return
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: 进入查询菜单")
            print("2: 进入添加菜单")
            print("3: 进入删除菜单")
            print("4: 进入修改菜单")
            print("5: 指定日期内销量统计功能")
            print("                                     其他数字退出")
            print("------------------------------------------------")
            cmd = input("请输入选项:").strip()
            if cmd=="1":
                self.metaQuery()
            elif cmd=="2":
                self.metaAdd()
            elif cmd=="3":
                self.metaDel()
            elif cmd=="4":
                self.metaModity()
            elif cmd=="5":
                generaloperat.statictic()
            else:
                break
            os.system("pause")
    def queryAllCommodity(self):
        generaloperat.queryAllCommodity()
    def queryAllCashier(self):
        '''前台 查询所有cashier的信息'''
        generaloperat.queryAllCashier()
    def queryAllPurchaser(self):
        '''前台 查询所有purchase'''
        generaloperat.queryAllPurchaser()
    def queryAllSell(self):
        '''前台 查询所有sell'''
        generaloperat.queryAllSell()
    def queryAllStock(self):
        '''前台'''
        generaloperat.queryAllStock()

    def addOneCashier(self):
        '''前台'''
        cash_no=input("请输入增加售货员的编号:").strip()
        cash=Basic.queryOneCashier(cash_no)
        if cash!=[]:
            print("该编号已存在不能重复添加.")
            return
        cash_name=input("请输入该员工的姓名:").strip()
        cash_pwd=input("请输入该员工的密码:").strip()
        cash_sex=input("请输入该员工的性别:").strip()
        cash_age=int(input("请输入该员工的年龄:").strip())
        cash_hourse=float(input("请输入该员工的日工作量:").strip())
        cash_salary=float(input("请输入该员工的月工资:").strip())
        cash_phone=input("请输入该员工的手机号:").strip()
        cash_entry=input("请输入该员工的出生日期(eg: 2019-6-4):").strip()
        try:
            Basic.addOneCashier(cash_no,cash_name,cash_pwd,cash_sex,cash_age,cash_hourse,cash_salary,cash_phone,cash_entry)
            print("添加售货员成功.")
        except Exception as e:
            print("添加售货员失败,原因:",e)

    def addOnePurchaser(self):
        ''''''
        pur_no=input("请输入增加进货员的编号:").strip()
        pur=Basic.queryOnePurchase(pur_no)
        if pur!=[]:
            print("该编号已存在不能重复添加.")
            return
        pur_name=input("请输入该员工的姓名:").strip()
        pur_sex=input("请输入该员工的性别:").strip()
        pur_age=int(input("请输入该员工的年龄:").strip())
        pur_salary=float(input("请输入该员工的月工资:").strip())
        pur_phone=input("请输入该员工的手机号:").strip()
        pur_entry=input("请输入该员工的出生日期(eg: 2019-6-4):").strip()
        try:
            Basic.addOnePurchaser(pur_no,pur_name,pur_sex,pur_age,pur_salary,pur_phone,pur_entry)
            print("添加进货员成功.")
        except Exception as e:
            print("添加进货员失败,原因:",e)
    def addOneCommodity(self):
        ''''''
        com_num = input("请输入要添加的商品编号:").strip()
        com = Basic.queryOneCommodity(com_num)
        if com != []:
            print("该商品已存在不能重复添加.")
            return
        com_name = input("请输入商品名称:").strip()
        com_type = input("请输入商品类型:").strip()
        com_size = input("请输入规格:").strip()
        com_price = float(input("请输入单价:").strip())
        com_mdate = input("请输入生产日期(格式 年-月-日):").strip()
        com_edate = input("请输入过期日期(格式 年-月-日):").strip()
        com_quantity = int(input("请输入库存数量:").strip())
        try:
            Basic.addOneCommodity(com_num, com_name, com_type, com_size, com_price, com_mdate, com_edate, com_quantity)
            print("添加商品成功")
        except Exception as e:
            print("添加商品失败,原因：", e)
    def delOneCashier(self):
        ''''''
        cash_no=input("请输入要移除的售货员的编号:").strip()
        cash=Basic.queryOneCashier(cash_no)
        if cash==[]:
            print("不存在该员工.")
            return
        cmd=input("确认移除该员工？(移除后所有与该员工有关的售货记录都会删除.y/n)").strip()
        if cmd[0]=='y'or cmd[0]=='Y':
            Basic.delOneCashier(cash_no)
            print("操作成功.")
        else:
            print("操作失败.")

    def delOnePurchaser(self):
        pur_no=input("请输入要移除的售货员的编号:").strip()
        pur=Basic.queryOnePurchase(pur_no)
        if pur==[]:
            print("不存在该员工.")
            return
        cmd=input("确认移除该员工？(移除后所有与该员工有关的进货记录都会删除.y/n)").strip()
        if cmd[0]=='y'or cmd[0]=='Y':
            Basic.delOnePurchase(pur_no)
            print("操作成功.")
        else:
            print("操作失败.")
    def delOneCommodity(self):
        ''''''
        com_no=input("请输入要移除的商品的编号:").strip()
        com=Basic.queryOneCommodity(com_no)
        if com==[]:
            print("不存在该商品.")
            return
        cmd=input("确认移除该商品？(移除后所有与该商品有关的进出货记录都会删除.y/n)").strip()
        if cmd[0]=='y'or cmd[0]=='Y':
            Basic.delOneCommodity(com_no)
            print("操作成功.")
        else:
            print("操作失败.")

    def modifyOneCashier(self):
        cash_no = input("请输入需要修改的售货员的编号:").strip()
        cash = Basic.queryOneCashier(cash_no)
        if cash == []:
            print("该售货员不存在.")
            return
        cash_name = input("请输入修改后的姓名:").strip()
        cash_pwd = input("请输入该员工的密码:").strip()
        cash_sex = input("请输入该员工的性别:").strip()
        cash_age = int(input("请输入该员工的年龄:").strip())
        cash_hourse = float(input("请输入该员工的日工作量:").strip())
        cash_salary = float(input("请输入该员工的月工资:").strip())
        cash_phone = input("请输入该员工的手机号:").strip()
        cash_entry = input("请输入该员工的出生日期(eg: 2019-6-4):").strip()
        try:
            Basic.modifyOneCashier(cash_no, cash_name, cash_pwd, cash_sex, cash_age, cash_hourse, cash_salary,
                                   cash_phone, cash_entry)
            print("修改成功.")
        except Exception as e:
            print("修改失败,原因:", e)

    def modifyOnePurchaser(self):
        pur_no = input("请输入需要修改的进货员的编号:").strip()
        pur = Basic.queryOnePurchase(pur_no)
        if pur == []:
            print("该售货员不存在.")
            return
        pur_name = input("请输入修改后的姓名:").strip()
        pur_sex = input("请输入该员工的性别:").strip()
        pur_age = int(input("请输入该员工的年龄:").strip())
        pur_salary = float(input("请输入该员工的月工资:").strip())
        pur_phone = input("请输入该员工的手机号:").strip()
        pur_entry = input("请输入该员工的出生日期(eg: 2019-6-4):").strip()
        try:
            Basic.modifyOnePurchaser(pur_no, pur_name, pur_sex, pur_age, pur_salary, pur_phone, pur_entry)
            print("修改成功.")
        except Exception as e:
            print("修改失败,原因:", e)

    def modifyOneCommodity(self):
        com_num = input("请输入要修改的商品编号:").strip()
        com = Basic.queryOneCommodity(com_num)
        if com == []:
            print("该商品不存在.")
            return
        com_name = input("请输入修改后的商品名称:").strip()
        com_type = input("请输入修改后的商品类型:").strip()
        com_size = input("请输入修改后的规格:").strip()
        com_price = float(input("请输入修改后的单价:").strip())
        com_mdate = input("请输入修改后的生产日期(格式 年-月-日):").strip()
        com_edate = input("请输入修改后的过期日期(格式 年-月-日):").strip()
        com_quantity = int(input("请输入修改后的库存数量:").strip())
        try:
            Basic.modifyOneCommodity(com_num, com_name, com_type, com_size, com_price, com_mdate, com_edate, com_quantity)
            print("修改商品成功")
        except Exception as e:
            print("修改商品失败,原因：", e)

