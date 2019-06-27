class Sell:
    def __init__(self,info):
        self.info=info
    def getComNo(self):
        return self.info[1]
    def getTime(self):
        return self.info[5]