from basic import Basic
from commodity import Commodity
from prettytable import PrettyTable
from purchaser import Purchaser
from cashier import Cashier
from datetime import datetime,timedelta
from sell import Sell
def queryAllCommodity():
    '''前台:查询所有商品信息'''
    info = Basic.queryAllCommodity()
    table = comm = Commodity.getTableaHead()
    for i in info:
        table.add_row(i)
    print(table)
    print("以上共 {} 条记录.".format(len(info)))


def queryOneCommodity():
    '''前台：查询一个商品信息'''
    com_num = input("请输入需要查询商品的编号:")
    res = Basic.queryOneCommodity(com_num)
    if not res:  # res为空
        print("没有该商品")
    else:
        table = comm = Commodity.getTableaHead()
        table.add_row(res)
        print(table, end="\n\n")
def queryOneCahier():
    cash_no=input("请输入需要查询的售货员的编号:").strip()
    cash=Basic.queryOneCashier(cash_no)
    if cash==[]:
        print("该售货员不存在.")
        return
    table=Commodity.getTableaHead()
    table.add_row(cash)
    print(table)
def queryOnePurchaser():
    pur_no=input("请输入需要查询的进货员的编号:").strip()
    pur=Basic.queryOnePurchase(pur_no)
    if pur==[]:
        print("该进货员不存在.")
        return
    table=Purchaser.getTableaHead()
    table.add_row(pur)
    print(table)

def queryAllStock():
    '''前台：查看所有进货信息'''
    info=Basic.queryAllStock()
    table=PrettyTable(["进货员编号","商品编号","进货流水号","进货单价","增加数量","进货日期"])
    for i in info:
        table.add_row(i)
    print(table)
    print("以上共 {} 条记录.".format(len(info)))
def queryAllCashier():
    '''前台 查询所有cashier的信息'''
    info=Basic.queryAllCashier()
    # print(info)
    table=Cashier.getTableaHead()
    # print(table)
    for i in info:
        table.add_row(i)
    print(table)
    print("以上共{}条记录.".format(len(info)))

def queryAllPurchaser():
    '''前台 查询所有purchase'''
    info=Basic.queryAllPurchaser()
    table=Purchaser.getTableaHead()
    for i in info:
        table.add_row(i)
    print(table)
    print("以上共{}条记录.".format(len(info)))
def queryAllSell():
    info=Basic.queryAllSell()
    table=PrettyTable(["收银员编号","商品编号","出售流水号","出售数量","总价","日期"])
    for i in info:
        table.add_row(i)
    print(table)
    print("以上共 {} 条记录.".format(len(info)))
def statictic():
    # try:
    left=input("请输入统计的开始日期:(例如:2017-8-6)").strip()
    left=datetime.strptime(left,"%Y-%m-%d").date()
    right=input("请输入统计的结束日期:(例如:2017-8-6)").strip()
    right = datetime.strptime(right, "%Y-%m-%d").date()
    cnt_list=getBothTopStatic(left,right,10)
    table=PrettyTable(["销量排行","商品编号","商品名称","类型","单价","指定日期内销量"])
    top=min(10,len(cnt_list))
    for i in range(0,top):
        ob=cnt_list[i].ob
        cnt=cnt_list[i].cnt
        table.add_row([i+1,ob.getNo(),ob.getName(),ob.getType(),ob.getPrice(),cnt])
    print(table)
    # except Exception as e:
    #     print("出错，原因:",e)
class pair:
    def __init__(self,ob=None,cnt=0):
        self.ob=ob
        self.cnt=cnt
def getBothTopStatic(left, right, com_no):
    '''返回列表 每个元素是一个商品对象和cnt'''
    all_sell=Basic.queryAllSell()
    cnt_dict={}
    for DA in all_sell:
        sell=Sell(DA)
        com_no=sell.getComNo()
        if com_no==None:
            continue
        now_date=sell.getTime().date()
        if now_date>=left and now_date <=right:
            cnt_dict.setdefault(com_no, 0)
            cnt_dict[com_no]+=1
    cnt_list=[]
    for com_num in cnt_dict:#key  编号,value is cnt
        ob=Basic.queryOneCommodity(com_num)
        cnt_list.append(pair(Commodity(ob),cnt_dict[com_num]))
    cnt_list.sort(key=lambda x:(x.cnt),reverse=True)
    return cnt_list