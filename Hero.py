class Hero(object):
    amt_of_scroll = 0
    amt_of_key = 0
    amt_of_pick = 0
    def __init__(self,name,amt_of_ap,num_of_str,num_of_dex,num_of_int,move,explore,exchange,attack,wait):
        #amt used for attributes that change, num used for attributes that dont change
        self.name = name
        self.amt_of_ap = amt_of_ap
        self.num_of_str = num_of_str
        self.num_of_dex = num_of_dex
        self.num_of_int = num_of_int
        self.move = move
        self.explore = explore
        self.exchange = exchange
        self.attack = attack
        self.wait = wait

    def moved(self):
        self.amt_of_ap -= self.move
    def exchanged(self):
        self.amt_of_ap -= self.exchange
    def attacked(self):
        self.amt_of_ap -= self.attack
    def waited(self):
        self.amt_of_ap -= self.wait
    def explored(self):
        self.amt_of_ap -= self.explore
    def getup(self):
        self.amt_of_ap-=1
    def allAttri(self):
        return ("Name: "+str(self.name)+"\nAP: "+str(self.amt_of_ap)+"\nSTR: "+str(self.num_of_str)+"\nDEX: "+str(self.num_of_dex)+"\nINT: "+str(self.num_of_int)+"\nMove: "+str(self.move)+"\nExplore: "+str(self.explore)+"\nExchange: "+str(self.exchange)+"\nAttack: "+str(self.attack)+"\nWait: "+str(self.wait))
    def pickPick(self):
        self.amt_of_ap-=self.num_of_str
        self.amt_of_pick+=1
    def pickKey(self):
        self.amt_of_ap-=self.num_of_dex
        self.amt_of_key += 1
    def pickScroll(self):
        self.amt_of_ap-=self.num_of_int
        self.amt_of_scroll += 1
    def breakBook(self):
        self.amt_of_ap-=1
    def breakGem(self):
        self.amt_of_ap-=1
    def breakHeart(self):
        self.amt_of_ap-=1
