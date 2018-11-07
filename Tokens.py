import Hero as h
#if it can break book and the hero goes to break the book then set states to brokens
class Tokens(object):
    book = False
    gem = False
    heart = False
    broken_book = True
    broken_gem = True
    broken_heart = True
    state_of_book = book
    state_of_gem = gem
    state_of_heart = heart
    def __init__(self, amt_of_scroll, amt_of_key, amt_of_pick):
        #amt used for attributes that change, num used for attributes that dont change
        self.amt_of_scroll = amt_of_scroll
        self.amt_of_key = amt_of_key
        self.amt_of_pick = amt_of_pick
    def canBreakBook(self):
        if(self.amt_of_scroll == 6):
            return True
        else:
            return False
    def canBreakGem(self):
        if(self.amt_of_key == 6):
            return True
        else:
            return False
    def canBreakHeart(self):
        if(self.amt_of_pick == 6):
            return True
        else:
            return False
