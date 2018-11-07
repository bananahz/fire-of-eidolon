import Hero as h
class HeroesCards():
    #Hero's name, AP, STR, DEX, INT, move, explore, attack, wait
    #CHECK HERO CLASS FOR ANY TOOLS METHODS YOU MIGHT NEED
    #THIS WILL HELP SAVE TIME
    amelia = h.Hero("Amelia", 3, 2, 3, 1, 1, 1, 1, 1, 1)
    aveloc = h.Hero("Aveloc", 3, 1, 3, 2, 1, 1, 1, 1, 1)
    sydney = h.Hero("Sydney and \"Bob\"", 3, 2, 2, 2, 1, 1, 1, 1, 1)
    tetemeko = h.Hero("Tetemeko", 3, 3, 2, 1, 1, 1, 1, 1, 1)
    cecilia = h.Hero("Cecilia", 3, 1, 3, 2, 1, 1, 1, 1, 1)
    kaylana = h.Hero("Kaylana", 3, 2, 1, 3, 1, 1, 1, 1, 1)
    kalistos = h.Hero("Kalistos", 3, 3, 1, 2, 1, 1, 1, 1, 1)
    daga = h.Hero("Daga", 3, 2, 3, 1, 1, 1, 1, 1, 1)
    cirrus = h.Hero("Cirrus", 3, 2, 1, 3, 1, 1, 1, 1, 1)
    carver = h.Hero("Carver", 3, 2, 2, 2, 1, 1, 1, 1, 1)
    aelfric = h.Hero("Aelfric", 3, 1, 2, 3, 1, 1, 1, 1, 1)
    sirus = h.Hero("Sirus", 3, 3, 2, 1, 1, 1, 1, 1, 1)














































    """def __init__(self):
        self.writeHeroes = open("Heroes.txt", "w")
        self.readHeroes = open("Heroes.txt", "r")

    def heroesF(self):
        with open("Heroes.txt", "w") as self.f:
            self.f.write("Amelia, AP: 3, STR: 2, DEX: 2, INT: 2, BLESS, SANCTIFY\n")
            self.f.write("Aveloc, AP: 3, STR: 1, DEX: 3, INT: 2, SOUL THIRST, CONSUME\n")
            self.f.write("Sydney and \"Bob\", AP: 3, STR: 2, DEX: 2,INT: 2, REMOTE CONTROL, METALLIC SACRIFICE\n")
            self.f
            .write("Tetemeko, AP: 3, STR: 3, DEX: 2, INT: 1, GEOPIVOT, TERRAPORT\n")
            self.f.write("Cecilia, AP: 3, STR: 1, DEX 3, INT: 2, SMITE, HOLY LIGHT\n")
            self.f.write("Kaylana, AP: 3, STR: 2, DEX: 1, INT: 3, RANGER'S SIGHT, MASTER FALCONY\n")
            self.f.write("Kalistos, AP: 3, STR: 3, DEX: 1, INT: 2, FIND SECRETS, SNEAK ATTACK\n")
            self.f.write("Daga, AP: 3, STR: 2, DEX: 3, INT: 1, MINDSTRIKE, TIMETURN\n")
            self.f.write("Cirrus, AP: 3, STR: 2, DEX: 1, INT: 3, ENORMOUS SWORD, BREAK LIMIT\n")
            self.f.write("Carver, AP: 3, STR: 2, DEX: 2, INT: 2, MYSTIC BOOMERANG, WALLCRACK BOMBS\n")
            self.f.write("Aelfric, AP: 3, STR: 1, DEX: 2, INT: 3, POLEARM LUNGE, HERO'S CHARGE\n")
            self.f.write("Sirus, AP: 3, STR: 3, DEX: 2, INT: 1, OBJECT PORTAL, TELEPORT\n")
            self.f.close()
        print (self.readHeroes.read())
        self.readHeroes.close()
    def getHeroesAttri(self,hero):
        hold = []
        with open("Heroes.txt","r") as f:
            chunk=[]
            print ("hello")
            for hero in f:
                print ("I"+chunk)
                chunk.append(hero)
        return chunk"""
