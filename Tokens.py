import Hero as h
#if it can break book and the hero goes to break the book then set states to brokens
class Tokens(object):
    # This is for when the states of these different attributes are not active yet
    book = False
    gem = False
    heart = False
    cant_get_eidolon = False
    # This is for when the states of these attributes are active
    broken_book = True
    broken_gem = True
    broken_heart = True
    can_get_eidolon = True
    # This is for checking the states of the actual attributes
    state_of_book = book
    state_of_gem = gem
    state_of_heart = heart
    state_of_eidolon = cant_get_eidolon
    def __init__(self, amt_of_scroll, amt_of_key, amt_of_pick):
        #amt used for attributes that change, num used for attributes that dont change
        self.amt_of_scroll = amt_of_scroll
        self.amt_of_key = amt_of_key
        self.amt_of_pick = amt_of_pick
    #This will check whether the books are breakable or not. DOES NOT MEAN THEY ARE AT THE LOCATION FOR BREAKING THE VORAX BOOK
    def canBreakBook(self):
        if(self.amt_of_scroll == 6):
            return True
        else:
            return False
    # This will check whether the gems are breakable or not. DOES NOT MEAN THEY ARE AT THE LOCATION FOR BREAKING THE VORAX GEM
    def canBreakGem(self):
        if(self.amt_of_key == 6):
            return True
        else:
            return False
    # This will check whether the hearts are breakable or not. DOES NOT MEAN THEY ARE AT THE LOCATION FOR BREAKING THE VORAX HEART
    def canBreakHeart(self):
        if(self.amt_of_pick == 6):
            return True
        else:
            return False

