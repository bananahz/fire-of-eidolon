import Hero as h
import Tokens as t
class HeroesCards():
    at_gem = False
    at_heart = False
    at_book = False
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
    #Send the hero attributes for scrolls, keys, and picks here
    def voraxTokens(self, amt_of_scroll, amt_of_key, amt_of_pick, at_gem, at_heart, at_book):
        tokens = t.Tokens(amt_of_scroll, amt_of_key, amt_of_pick)
        self.at_gem = at_gem
        self.at_heart = at_heart
        self.at_book = at_book
        if(tokens.state_of_gem == tokens.broken_gem and tokens.state_of_heart == tokens.broken_heart and tokens.state_of_book == tokens.broken_book):
            tokens.state_of_eidolon = tokens.can_get_eidolon
        else:
            if(at_gem == True and tokens.canBreakGem()):
                tokens.state_of_gem = tokens.broken_gem
            else:
                tokens.state_of_gem = tokens.gem
            if (at_heart == True and tokens.canBreakHeart()):
                tokens.state_of_heart = tokens.broken_heart
            else:
                tokens.state_of_heart = tokens.heart
            if (at_book == True and tokens.canBreakBook()):
                tokens.state_of_book = tokens.broken_book
            else:
                tokens.state_of_book = tokens.book

