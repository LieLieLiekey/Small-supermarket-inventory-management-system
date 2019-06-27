from prettytable import PrettyTable
class Purchaser:
    def __init__(self,info_list=None):
        self.info=info_list
    def getNo(self):
        return self.info[0]
    def getName(self):
        return self.info[1]
    def getSex(self):
        return self.info[2]
    def getAge(self):
        return self.info[3]
    def getSalary(self):
        return self.info[4]
    def getPhone(self):
        return self.info[5]
    def getEntrytime(self):
        return self.info[6]
    @classmethod
    def getTableaHead(cls):
        return  PrettyTable(["进货员编号", "姓名","性别","年龄",r"工资/月","手机号","出生日期"])


