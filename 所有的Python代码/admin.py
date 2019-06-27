class Admin:
    def __init__(self,info):
        self.info=info
    def getNo(self):
        return self.info[0]
    def getPwd(self):
        return self.info[1]