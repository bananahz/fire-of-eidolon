import os, pygame, random


class Cards:
    scale = .4
    all_cards = {}
    current_deck = []
    showing_deck = []
    void_deck = []

    def __init__(self):
        pygame.init()
        self.load()
        self.shuffle()

    # loads all card images in a dictionary, and created a current_deck list
    def load(self):
        items = os.listdir("Textures/Cards")
        for name in items:
            if name.endswith(".png"):
                image = pygame.image.load("Textures/Cards/" + name)
                self.all_cards[name[:len(name) - 4]] = pygame.transform.scale(image,
                    (int(image.get_size()[0] * self.scale),
                     int(image.get_size()[1] * self.scale)))
                if name != "RitualCardBack.png":
                    self.current_deck.append(name[:len(name) - 4])

    #shuffles current deck of cards
    def shuffle(self):
        random.shuffle(self.current_deck)

    #returns list of cards needed
    def draw(self, draw_number):
        draw_list = []
        for i in range(draw_number):
            if len(self.current_deck) == 0:
                self.out_of_cards()
            draw_list.append(self.current_deck[0])
            self.current_deck.pop(0)
        return draw_list

    #use this to get card image
    def get_card_image(self, card_name):
        return self.all_cards[card_name]

    #sends card to void
    def void_card(self, card_name):
        self.void_deck.append(card_name)
        self.current_deck.remove(card_name)

    #adds cards not in void to current deck
    def out_of_cards(self):
        for key in self.all_cards:
            if key not in self.void_deck:
                self.current_deck.append(key)
