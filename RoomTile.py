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

    def __init__(self, name):  # vestibule, special rooms
        pygame.init()
        self.name = name
        self.image = pygame.image.load("Textures/Rooms/" + name + ".png")
        self.locked = False

    def __init__(self, name, color, doorways):
        # normal rooms
        super(RoomTile, self).__init__()
        self.color = color
        self.doorways = doorways
        self.token = ""
        self.cultist = 0
        self.players = []
        self.banished = False

    """def get_name(self):
       return self.name

   def get_type(self):
       return self.type

   def color(self):
       return self.color

   def doorways(self):
       return self.doorways

   def token(self):
       return self.token

   def add_cultist(self):
       self.cultist = True

   def has_cultist(self):
       return self.cultist

   def add_players(self, players):
       self.players = players

   def players(self, []):
       return self.players

   def set_banished(self):
       self.banished = True

   def banished(self):
       return self.banished

   def set_rotation(self, image, rotation):
       # sprite rotation
       return

   def get_image(self):
       return self.image

   def rotation(self):
       return self.rotation """

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







