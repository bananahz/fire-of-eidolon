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

import os, pygame, random, RoomTile as r


class Room:
    scale = .4
    all_rooms = []
    current_deck = []  # normal mode
    void_deck = []

    def __init__(self):
        pygame.init()
        self.load()
        self.shuffle()

    # load attributes
    def load(self):

        AcidJets = r.RoomTile("AcidJets", "green", ["north", "south"])
        ArrowTrap = r.RoomTile("ArrowTrap", "green", ["east, west, south"])
        DarkSlime = r.RoomTile("DarkSlime", "red", ["east", "south"])
        DenOfSnakes = r.RoomTile("DenOfSnakes", "green", ["north", "east", "south"])
        Dragonling = r.RoomTile("Dragonling", "red", ["north", "east", "south"])
        FelKnight = r.RoomTile("FelKnight", "red", ["north", "east", "south"])
        FloatingStones = r.RoomTile("FloatingStones", "green", ["north", "south", "east", "west"])
        HallOfIllusion = r.RoomTile("HallOfIllusion", "blue", ["east", "south"])
        LaughingShadow = r.RoomTile("LaughingShadow", "blue", ["north", "east", "west", "south"])
        LavaLake = r.RoomTile("LavaLake", "green", ["west", "south"])
        MindEater = r.RoomTile("MindEater", "green", ["east", "west", "south"])
        Minotaur = r.RoomTile("Minotaur", "blue", ["north", "south", "east", "west"])
        MimicChest = r.RoomTile("MimicChest", "blue", ["south"])
        OgreBrute = r.RoomTile("OgreBrute", "red", ["west", "south"])
        ParadoxPuzzle = r.RoomTile("ParadoxPuzzle", "blue", ["north", "west", "south"])
        PendulumBlades = r.RoomTile("PendulumBlades", "green", ["north", "south"])
        Psychomancer = r.RoomTile("Psychomancer", "blue", ["north", "east", "west", "south"])
        SkeletalGuards = r.RoomTile("SkeletalGuards", "red", ["north", "south"])
        SphynxsRiddle = r.RoomTile("SphynxsRiddle", "blue", ["north", "south"])
        SpikedPit = r.RoomTile("SpikedPit", "green", ["north", "east", "south"])
        VoraciousPlant = r.RoomTile("VoraciousPlant", "red", ["north", "east", "west", "south"])

        Blank = r.RoomTile("Blank")
        FireOfEidolon = r.RoomTile("FireOfEidolon")
        VoraxsHeart = r.RoomTile("VoraxsHeart")
        VoraxsFocus = r.RoomTile("VoraxsFocus")
        VoraxsKnowledge = r.RoomTile("VoraxsKnowledge")
        Vestibule = r.RoomTile("Vestibule")
        SecretPassageX = r.RoomTile("SecretPassageX")
        SecretPassageY = r.RoomTile("SecretPassageY")
        NewExit = r.RoomTile("NewExit")
        BackOfCard = r.RoomTile("BackOfCard")

        # normal for now
        self.all_rooms = {"Blank": Blank , "FireOfEidolon":FireOfEidolon, "VoraxsFocus":VoraxsFocus, "VoraxsHeart":VoraxsHeart, "VoraxsKnowledge":VoraxsKnowledge,
                              "AcidJets": AcidJets, "ArrowTrap":ArrowTrap, "DarkSlime":DarkSlime, "DenOfSnakes":DenOfSnakes, "Dragonling":Dragonling,
                              "FelKnight":FelKnight, "FloatingStones":FloatingStones, "HallOfIllusion":HallOfIllusion, "LaughingShadow":LaughingShadow,
                              "LavaLake":LavaLake, "MindEater":MindEater, "Minotaur":Minotaur, "MimicChest":MimicChest, "OgreBrute":OgreBrute,
                              "ParadoxPuzzle":ParadoxPuzzle, "PendulumBlades":PendulumBlades, "Psychomacer":Psychomancer, "SkeletalGuards":SkeletalGuards,
                              "SphynxsRiddle":SphynxsRiddle, "SpikedPit":SpikedPit, "VoraciousPlant":VoraciousPlant, "Vestibule":Vestibule, "BackOfCard":BackOfCard}

        self.current_deck = [FireOfEidolon, VoraxsFocus, VoraxsHeart, VoraxsKnowledge,
                             AcidJets, ArrowTrap, DarkSlime, DenOfSnakes, Dragonling,
                             FelKnight, FloatingStones, HallOfIllusion, LaughingShadow,
                             LavaLake, MindEater, Minotaur, MimicChest, OgreBrute,
                             ParadoxPuzzle, PendulumBlades, Psychomancer, SkeletalGuards,
                             SphynxsRiddle, SpikedPit, VoraciousPlant]

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

