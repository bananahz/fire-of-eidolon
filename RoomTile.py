import os, pygame, random


# string name
# string color
# list of open doorways
# string token
# boolean cultist
# list players on room
# boolean banished
# int rotation
# book, heart, gem

class RoomTile(pygame.sprite.Sprite):
    name = ""
    color = ""
    doorways = []
    token = "" # key - green, pick - red, scroll - blue
    cultist = 0
    players = []
    banished = False
    image = pygame.image.load("Textures/Rooms/Blank.png")
    # for voraxs
    locked = False

    def __init__(self, name, color="none", doorways=["north", "east", "west", "south"]):
        # normal rooms
        super(RoomTile, self).__init__()
        self.name = name
        self.image = pygame.image.load("Textures/Rooms/" + name + ".png")
        self.locked = False
        self.color = color
        self.doorways = doorways
        self.token = ""
        self.cultist = 0
        self.players = []
        self.banished = False

    def rotation(self):
        original = self.image
        self.image = pygame.transform.rotate(original, 90)
        for x in range (len(self.doorways)) :
            if self.doorways[x] == "north" :
                self.doorways[x] = "east"
            elif self.doorways[x] == "east":
                self.doorways[x] = "south"
            elif self.doorways[x] == "south" :
                self.doorways[x] = "west"
            elif self.doorways[x] == "west" :
                self.doorways[x] = "north"
            else :
                continue
