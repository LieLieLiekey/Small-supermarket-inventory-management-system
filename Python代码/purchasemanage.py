from basic import Basic
from commodity import  Commodity
from prettytable import PrettyTable
from purchaser import Purchaser
import os
import generaloperat
from purchaser import Purchaser
class PurchaseManage:
    def __init__(self):
        self.admin=None
    def login(self):
        '''带前台的登陆界面'''
        pur_num=input("请输入您的编号:").strip()
        pur=Basic.queryOnePurchase(pur_num)
        if not pur:
            print("不存在该编号.")
            return False
        else:
            self.admin=Purchaser(pur)
            return True
    def meta(self):
        '''操作选项界面'''
        if not self.login():
            return
        while True:
            os.system("cls")
            print("------------------------------------------------")
            print("1: 查询单个商品信息")
            print("2: 查看所有商品信息")
            print("3: 添加商品信息")
            print("4: 查看所有进货信息")
            print("5: 进货")
            print("                                     其他数字退出")
            print("------------------------------------------------")
            cmd = input("请输入选项:").strip()
            if cmd=="1":
                self.queryOne()
            elif cmd=="2":
                self.queryAll()
            elif cmd=="3":
                self.addOne()
            elif cmd=="4":
                self.querAllStock()
            elif cmd=="5":
                self.purchase()
            else:
                self.admin=None
                break
            os.system("pause")
    def querAllStock(self):
        generaloperat.queryAllStock()
    def addOne(self):
        '''前台 添加一个新的商品，库存数量为0'''
        com_num=input("请输入要添加的商品编号:").strip()
        com=Basic.queryOneCommodity(com_num)
        if com!=[]:
            print("该商品已存在不能重复添加.")
            return
        com_name=input("请输入商品名称:").strip()
        com_type=input("请输入商品类型:").strip()
        com_size=input("请输入规格:").strip()
        com_price=float(input("请输入单价:").strip())
        com_mdate=input("请输入生产日期(格式 年-月-日):").strip()
        com_edate=input("请输入过期日期(格式 年-月-日):").strip()
        com_quantity=0
        try:
            Basic.addOneCommodity(com_num,com_name,com_type,com_size,com_price,com_mdate,com_edate,com_quantity)
            print("添加成功")
        except Exception as e:
            print("添加失败,原因：",e)
    def purchase(self):
        '''前台 进货'''
        com_num=input("请输入要进货的商品编号:").strip()
        com=Basic.queryOneCommodity(com_num)
        if com==[]:
            print("该商品不存在，请先添加该商品.")
            return
        com_cnt=int(input("请输入进货的数量:").strip())
        com_price = float(input("请输入进货的单价:").strip())
        in_date = input("请输入进货日期(格式 年-月-日):").strip()
        try:
            num=self.getFlowNum()
            Basic.addOneStock(self.admin.getNo(), com_num, num, com_price, com_cnt, in_date)
            Basic.addOneCommodityCnt(com_num,com_cnt)
            print("操作成功.")
        except Exception as e:
            print("操作失败，原因：",e)

    def queryAll(self):
        '''前台 查看所有商品信息'''
        generaloperat.queryAllCommodity()
    def queryOne(self):
        '''前台 查看一个商品信息'''
        generaloperat.queryOneCommodity()
    def exitlogin(self):
        '''前台 退出登陆 ，保证已经登陆'''
        self.admin=None
    def getFlowNum(self):
        while True:
            num=Basic.getFlowNum()
            info=Basic.queryOneStockFlowNum(num)
            if info==[]:
                return num