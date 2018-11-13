import pygame
class Hero(object):
    pygame.init()
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
    #For when the player MOVES INTO A NEW ROOM
    def moved(self):
        self.amt_of_ap -= self.move
    #For when the player exchanges a material with another player
    def exchanged(self):
        self.amt_of_ap -= self.exchange
    #For when the player attacks a cultist
    def attacked(self):
        self.amt_of_ap -= self.attack
    #For when player skips their turn
    def waited(self):
        self.amt_of_ap -= self.wait
    #For when the player PUTS DOWN A NEW ROOM
    def explored(self):
        self.amt_of_ap -= self.explore
    #For when play gets up after being kicked from a cultist destroyed room
    def getup(self):
        self.amt_of_ap-=1
    #Returns all attributes
    def allAttri(self):
        return ("Name: "+str(self.name)+"\nAP: "+str(self.amt_of_ap)+"\nSTR: "+str(self.num_of_str)+"\nDEX: "+str(self.num_of_dex)+"\nINT: "+str(self.num_of_int)+"\nMove: "+str(self.move)+"\nExplore: "+str(self.explore)+"\nExchange: "+str(self.exchange)+"\nAttack: "+str(self.attack)+"\nWait: "+str(self.wait))
    #For when the player picks up a pick
    def pickPick(self):
        self.amt_of_ap-=self.num_of_str
        self.amt_of_pick+=1
    #For when the player picks up a key
    def pickKey(self):
        self.amt_of_ap-=self.num_of_dex
        self.amt_of_key += 1
    #For when the player picks up a scroll
    def pickScroll(self):
        self.amt_of_ap-=self.num_of_int
        self.amt_of_scroll += 1
    #For when the player breaks the vorax book room
    def breaksBook(self):
        self.amt_of_ap-=1
    #For when the player breaks the vorax gem room
    def breaksGem(self):
        self.amt_of_ap-=1
    #For when the player breaks the vorax heart room
    def breaksHeart(self):
        self.amt_of_ap-=1
    def getImage(self,name):
        if(name == "Aelfric" or name == "Cecelia" or name == "Cirrus"):
            return pygame.image.load("Textures/Heroes/Combat/"+name+".png")
        elif (name == "Kalistos" or name == "Tetemeko"):
            return pygame.image.load("Textures/Heroes/Movement/" + name + ".png")
        elif (name == "Amelia" or name == "Daga" or name == "Sydney"):
            return pygame.image.load("Textures/Heroes/Room Control/" + name + ".png")
        elif (name == "Aveloc"):
            return pygame.image.load("Textures/Heroes/Specialist/Aveloc.png")
        elif (name == "Carver" or name == "Kaylana" or name == "Sirus"):
            return pygame.image.load("Textures/Heroes/Utility/" + name + ".png")
