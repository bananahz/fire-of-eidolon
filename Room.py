"""
Boolean for whether or not it has a token
Boolean for whether or not it has a cultist
Boolean for whether or not it has a hero?
If its a lock, boolean for whether or not the lock was broken
-Maybe int for whether it’s blue, red, green, or a lock? (Ex: 0 - blue, 4 - blueLock?)
-Needs int for # of doorways
-Also for rotation, maybe int rot = up; (up = 0(or 0 degrees), right = 1(or 90 degrees), down = 2(or 180 or 90*2)) 
 That way you could multiply a 90 degree rotation for the int number for the rotation
-String name

1. have rooms display in right corner, shuffled
2. when a card is clicked, be able to change orientation and position placed 
"""

import os, pygame, random, Room as r


class Room:
    scale = .4
    all_rooms = {}
    current_deck = []  # normal mode
    void_deck = []

    def __init__(self):
        pygame.init()
        self.load()
        self.shuffle()

    # load attributes
    def load(self):

        AcidJets = r.Room("AcidJets", "green", ["north", "south"])
        ArrowTrap = r.Room("ArrowTrap", "green", ["east, west, south"])
        DarkSlime = r.Room("DarkSlime", "red", ["east", "south"])
        DenOfSnakes = r.Room("DenOfSnakes", "green", ["north", "east", "south"])
        Dragonling = r.Room("Dragonling", "red", ["north", "east", "south"])
        FelKnight = r.Room("FelKnight", "red", ["north", "east", "south"])
        FloatingStones = r.Room("FloatingStones", "green", ["north", "south", "east", "west"])
        HallOfIllusion = r.Room("HallOfIllusion", "blue", ["east", "south"])
        LaughingShadow = r.Room("LaughingShadow", "blue", ["north", "east", "west", "south"])
        LavaLake = r.Room("LavaLake", "green", ["west", "south"]),
        MindEater = r.Room("MindEater", "green", ["east", "west", "south"])
        Minotaur = r.Room("Minotaur", "blue", ["north", "south", "east", "west"])
        MimicChest = r.Room("MimicChest", "blue", ["south"])
        OgreBrute = r.Room("OgreBrute", "red", ["west", "south"])
        ParadoxPuzzle = r.Room("ParadoxPuzzle", "blue", ["north", "west", "south"])
        PendulumBlades = r.Room("PendulumBlades", "green", ["north", "south"])
        Psychomancer = r.Room("Psychomancer", "blue", ["north", "east", "west", "south"])
        SkeletalGuards = r.Room("SkeletalGuards", "red", ["north", "south"])
        SphynxsRiddle = r.Room("SphynxsRiddle", "blue", ["north", "south"])
        SpikedPit = r.Room("SpikedPit", "green", ["north", "east", "south"])
        VoraciousPlant = r.Room("VoraciousPlant", "red", ["north", "east", "west", "south"])

        Blank = r.Room("Blank")
        FireOfEidolon = r.Room("FireOfEidolon")
        VoraxsHeart = r.Room("VoraxsHeart")
        VoraxsFocus = r.Room("VoraxsFocus")
        VoraxsKnowledge = r.Room("VoraxsKnowledge")
        Vestibule = r.Room("Vestibule")
        SecretPassageX = r.Room("SecretPassageX")
        SecretPassageY = r.Room("SecretPassageY")
        NewExit = r.Room("NewExit")


        #normal for now
        self.current_deck.append(Blank, FireOfEidolon, VoraxsFocus, VoraxsHeart, VoraxsKnowledge,
                                 AcidJets, ArrowTrap, DarkSlime, DenOfSnakes, Dragonling,
                                 FelKnight, FloatingStones, HallOfIllusion, LaughingShadow,
                                 LavaLake, MindEater, Minotaur, MimicChest, OgreBrute,
                                 ParadoxPuzzle, PendulumBlades, Psychomancer, SkeletalGuards,
                                 SphynxsRiddle, SpikedPit, VoraciousPlant)

    # shuffles current deck of rooms
    def shuffle(self):
        random.shuffle(self.current_deck)

    def next_room(self):
        top_room = self.current_deck.pop(0)
        self.current_deck.append(top_room)

    def draw(self):
        draw_list = []
        if len(self.current_deck) == 0:
            self.out_of_rooms()
        draw_list.append(self.current_deck[0])
        self.current_deck.pop(0)
        return draw_list

    # use this to get room image
    def get_room_image(self, room_name):
        return self.all_rooms[room_name]

    # sends rooms to void
    def void_card(self, room_name):
        self.void_deck.append(room_name)
        self.current_deck.remove(room_name)

    # adds rooms not in void to current deck
    def out_of_rooms(self):
        for key in self.all_rooms:
            if key not in self.void_deck:
                self.current_deck.append(key)


