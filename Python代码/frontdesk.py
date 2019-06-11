from basic import Basic
from commodity import  Commodity
from prettytable import PrettyTable
from cashier import Cashier
import os
class ShopCar:
    '''储存商品对象和购买数量
    '''
    def __init__(self):
        self.shop_list=[]
    def addCommodity(self,com,com_cnt):#传入商品信息和购买数量
        ''' *保证库存肯定是有货的
        商品重复则直接添加数量,否则添加到列表即可
        '''
        com_no=com.getNo()
        for i in range(len(self.shop_list)):
            now_com=self.shop_list[i][0]
            if now_com.getNo()==com_no:
                self.shop_list[i][1]+=com_cnt
                return
        #购物车不存在该商品
        self.shop_list.append([com,com_cnt])
        return
    def delCommodity(self,com_num,com_cnt):
        '''保证满足
        '''
        for i in range(len(self.shop_list)):
            now_com=self.shop_list[i][0]
            if now_com.getNo()==com_num:
                self.shop_list[i][1]-=com_cnt
                if self.shop_list[i][1]==0:
                    self.shop_list.pop(i)
                return
    def clear(self):
        '''清空购物车'''
        self.shop_list.clear()

    def getMonery(self):
        '''得到总钱数'''
        res=0.0
        for com,cnt in self.shop_list:
            res+=com.getPrice()*cnt
        return res
    def getCommodityCnt(self,com_num):
        '''返回商品编号对应的数量'''
        res=0
        for com,cnt in self.shop_list:
            if com.getNo()==com_num:
                res=cnt
                break
        return res
    def printList(self):
        '''打印当前购物车信息
        ["商品编号", "商品名称", "商品类型","规格","单价","购买数量"]
        '''
        table=PrettyTable(["商品编号", "商品名称", "商品类型","规格","单价","购买数量"])
        for com, cnt in self.shop_list:
            table.add_row([com.getNo(),com.getName(),com.getType(),com.getSize(),com.getPrice(),cnt])
        print(table)
        print("总价：",self.getMonery(),end="\n\n")
    def getlist(self):
        ''' 返回购买信息'''
        # res_list=[]
        # for i in self.shop_list:
        #     com=i[0]
        #     cnt=i[2]
        #     res_list.append((com.getNo(),cnt))#返回商品编号和 购买的数量
        # return res_list
        return self.shop_list
    def empty(self):
        if not self.shop_list:
            return True
        return False
class FrontDesk:
    '''前台控制'''
    def __init__(self):
        self.admin=None
        self.car=ShopCar()
    def exitLogin(self):
        print("账号 {} 已经退出登陆.".format(self.admin.getNo()))
        self.admin=None

    def meta(self):
        '''前台:菜单'''
        if self.login()==False:
            return
        while(True):
            os.system("cls")
            print("------------------------------------------------")
            print("1: 查询单个商品信息")
            print("2: 查看所有商品信息")
            print("3: 购买功能")
            if self.admin!=None:
                print("4: 退出登录")
            print("                                     其他数字退出")
            print("------------------------------------------------")
            cmd=input("请输入选项:").strip()
            if cmd=="1":
                self.queryOne()
            elif cmd=="2":
                self.queryAll()
            elif cmd=="3":
                if (self.admin!=None) or self.login():
                    self.shopingMeta()
            elif self.admin!=None and cmd=="4":
                self.exitLogin()
                break
            else:
                break
            os.system("pause")
    def login(self):
        '''前台:admin登陆'''
        in_num=input("请输入您的账号:").strip()
        cash=Basic.queryOneCashier(in_num)
        if not cash:
            print("不存在该账号.")
            return  False
        cashier=Cashier(cash)
        in_pwd=input("请输入您的密码:").strip()
        if cashier.getPwd()==in_pwd:
            self.admin=cashier
            print("登陆成功.")
            return True
        else:
            print("密码错误.")
            return False
    def queryAll(self):
        '''前台:查询所有商品信息'''
        info=Basic.queryAllCommodity()
        table = comm = Commodity.getTableaHead()
        for i in info:
            table.add_row(i)
        print(table)
        print("以上共 {} 条记录.".format(len(info)))
    def queryOne(self):
        '''前台：查询一个商品信息'''
        com_num=input("请输入需要查询商品的编号:")
        res=Basic.queryOneCommodity(com_num)
        if not res:#res为空
            print("没有该商品")
        else:
            table=comm=Commodity.getTableaHead()
            table.add_row(res)
            print(table,end="\n\n")
    def shopingMeta(self):
        '''前台：购买'''
        while True:
            os.system("cls")
            print("当前购物车:")
            self.car.printList()
            print("-------\n")
            print("1:向购物车中添加商品")
            print("2:从购物车中删除商品")
            print("3:清空购物车")
            print("4:结算")
            print("--------------------其他选项退出")
            cmd=input("请输入选项:").strip()
            if cmd=="1":
                self.addCom()
            elif cmd=="2":
                self.delCom()
            elif cmd=="3":
                self.clearShopCar()
            elif cmd=="4":
                self.pay()
            else:
                break
            os.system("pause")
    def addCom(self):
        '''前台: 添加购物车 '''
        com_num=input("请输入商品编号:").strip()
        com_info=Basic.queryOneCommodity(com_num)
        if not com_info:
            print("商品不存在.")
            return
        com=Commodity(com_info)
        com_cnt=int(input("请输入商品数量:").strip())
        if com_cnt <=0:
            print("购买数量必须大于0.")
            return
        if com_cnt>com.getQuantiy() :
            print("商品库存不足.")
        else :
            self.car.addCommodity(com,com_cnt)
            print("添加进入购物车成功.")

    def clearShopCar(self):
        '''前台：清空购物车'''
        cmd=input("输入 1 确认清空购物车:").strip()
        if cmd=="1":
            self.car.clear()
            print("购物车已清空.")
        else:
            print("操作已取消.")

    def delCom(self):
        '''前台：删除购物车某一个物品'''
        com_num = input("请输入商品编号:").strip()
        have_cnt=self.car.getCommodityCnt(com_num)
        if have_cnt==0:
            print("购物车中无该商品")
        else:
            del_cnt=int(input("购物车中该商品有 {} 个,请输入需要删除该商品的数量:".format(have_cnt)).strip())
            self.car.delCommodity(com_num,min(del_cnt,have_cnt))
            print("删除成功.")
    def getFlowNum(self):
        while True:
            num=Basic.getFlowNum()
            info=Basic.queryOneSellFlowNum(num)
            if info==[]:
                return num
    def pay(self):
         '''前台:结算'''
         if self.car.empty():
             print("购物车是空的.")
             return
         all_money=self.car.getMonery()
         pay_money=float(input("请支付{}元:".format(all_money)).strip())
         if pay_money<all_money :
             print("支付失败.")
         else:
             print("支付成功,找零{}元. ".format(pay_money-all_money))
             shop_list=self.car.getlist()
             for com,com_cnt in shop_list:
                 #删除库存数量
                 Basic.delCommodityCnt(com.getNo(),com_cnt)
                 #添加购买信息
                 num=self.getFlowNum()
                 Basic.addOneSell(self.admin.getNo(),com.getNo(),num,com_cnt,com.getPrice()*com_cnt)
             print("您已经成功购买以下商品,支付{}元 ,找零{}元 .".format(pay_money,pay_money-all_money))
             self.car.printList()
             self.car.clear()



