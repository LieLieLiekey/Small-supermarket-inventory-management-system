from prettytable import PrettyTable
class Cashier:
    def __init__(self,info_list=None):
        self.info=info_list
    def getNo(self):
        return self.info[0]
    def getName(self):
        return self.info[1]
    def getPwd(self):
        return self.info[2]
    def getSex(self):
        return self.info[3]
    def getAge(self):
        return self.info[4]
    def getHourse(self):
        return self.info[5]
    def getSalary(self):
        return self.info[6]
    def getPhone(self):
        return self.info[7]
    def getEntrytime(self):
        return self.info[8]
    @classmethod
    def getTableaHead(cls):
        return  PrettyTable(["售货员编号", "姓名", "密码","性别","年龄","Hourse",r"工资/月","手机号","出生日期"])


