# logic
import Cards as c, Room as r, Difficulty as d, HeroesCards as h, random
from random import shuffle


class Game:
    room_class = None
    map = []
    main_room = None
    current_player = None
    current_card_list = []
    void_deck = []
    difficulty_level = None
    player_list = []
    card_class = None


    def __init__(self):
        self.room_class = r.Room()
        self.map = [[self.room_class.all_rooms.get("Vestibule")]]
        self.main_room = (0, 0)
        self.difficulty_level = d.All_Difficulties().difficulties.get("Normal")  # random diff for now
        self.player_list = [h.HeroesCards.aelfric, h.HeroesCards.cecilia,
                            h.HeroesCards.tetemeko]  # random players for now
        self.current_player = self.player_list[0]
        self.map[0][0].players = self.player_list
        self.card_class = c.Cards()


    def draw_cards_diff(self):
        dc = self.difficulty_level.current_draw_count
        for x in range(dc):
            if len(self.card_class.current_deck) > 0:
                self.card_class.showing_deck.insert(0, self.card_class.current_deck.pop())
                self.add_cultist(self.card_class.showing_deck[0])
            elif len(self.card_class.current_deck) == 0:
                self.card_class.current_deck = self.card_class.showing_deck
                self.card_class.shuffle()
                self.card_class.showing_deck = []
                self.difficulty_level.go_up()

   def player_actions(self, action):
    xPos = 0
    yPos = 0
    current_tile = self.map[0][0]

    for x in range(len(self.map)):
        for i in range(len(self.map[0])):
            print("current player: " + str(self.current_player.name))
            print("current tile: " + str(self.map[x][i].name))
            print("players_list on tile: " + str(self.map[x][i].players))
            if self.current_player in self.map[x][i].players:
                current_tile = self.map[x][i]
                xPos = x
                yPos = i
    if self.current_player.amt_of_ap > 0:
        if action == 'w':
            if yPos - 1 > -1:
                self.map[xPos][yPos].players.remove(self.current_player)
                self.map[xPos][yPos - 1].players.append(self.current_player)
                self.current_player.amt_of_ap -= 1
        if action == 'a':
            if xPos - 1 > -1:
                self.map[xPos][yPos].players.remove(self.current_player)
                self.map[xPos - 1][yPos].players.append(self.current_player)
                self.current_player.amt_of_ap -= 1
        if action == 's':
            if yPos + 1 < len(self.map[0]):
                self.map[xPos][yPos].players.remove(self.current_player)
                self.map[xPos][yPos + 1].players.append(self.current_player)
                self.current_player.amt_of_ap -= 1
        if action == 'd':
            if xPos + 1 < len(self.map):
                self.map[xPos][yPos].players.remove(self.current_player)
                self.map[xPos + 1][yPos].players.append(self.current_player)
                self.current_player.amt_of_ap -= 1
        if action == 'Wait':
            self.current_player.amt_of_ap -= 1
    elif self.current_player.amt_of_ap == 0:
        self.change_player_turn(self.player_list)
        # repeat for other keys
        """if action == "pick_token" and self.map[xPos][yPos].token != None:
            if self.map[xPos][yPos].token == "green token":
                return
                if self.current_player.amt_of_ap > 0:
            if action == 'w':
                if self.map[yPos + 1] > -1:
                    self.map[xPos][yPos + 1].players.append(player)

            # repeat for other keys
            if action == "collect_token" and current_tile.token != None:
                if current_tile.token == "key" and  # (4 - self.current_player.amt_of_ap):
                    self.current_player

            if action == 'explore':
                pass
                # add new room if possible
            if action == 'attack' and current_tile.cultist != 0:
                current_tile.cultist -= 1
            if action == 'exchange' and len(current_tile.players) > 1:
                pass
                # add ui to exchange tokens
            if action == 'skill':
                # do player stuff
                pass
            if action == 'wait':
                # start cultist phase
                pass
            if action == "destroy_relic":
                pass
            if action == "retrieve_fire":
                pass"""
    # adds room tile to map

    def add_cultist(self, name_of_room):
        for y in self.map:
            for x in y:
                if x.name == name_of_room:
                    x.cultist += 1
                    if x.cultist >= 2:
                        self.remove_from_map(x)
                        self.room_class.void_card(x)
                        for l in range(2):
                            self.card_class.void_card(x)
                            self.card_class.current_deck.remove(x)
                            self.card_class.showing_deck.remove(x)

    #adds room tile to map
    def add_to_map(self, position, room):
        valid = self.place_valid(position, room)
        if valid[0]:
            if valid[1] == "north":
                if position[0]<0:
                    li = [None] * len(self.map[0])
                    li[position[1]] = room
                    self.map.insert(0, li)
                    self.main_room = (self.main_room[0] + 1, self.main_room[1])
                else:
                    self.map[position[0]][position[1]] = room
            if valid[1] == "south":
                if position[0] >= len(self.map):
                    li = [None] * len(self.map[0])
                    li[position[1]] = room
                    self.map.append(li)
                else:
                    self.map[position[0]][position[1]] = room
            if valid[1] == "east":
                if position[1] >= len(self.map[0]):
                    for x in range(len(self.map)):
                        if x == position[0]:
                            self.map[x].append(room)
                        else:
                            self.map[x].append(None)
                else:
                    self.map[position[0]][position[1]] = room
            if valid[1] == "west":
                if position[1] < 0:
                    for x in range(len(self.map)):
                        if x == position[0]:
                            self.map[x].insert(0, room)
                        else:
                            self.map[x].insert(0, None)
                    self.main_room = (self.main_room[0], self.main_room[1]+1)
                else:
                    self.map[position[0]][position[1]] = room
            return True
        else:
            return False

    # placement of tile is valid and direction from tile
    def place_valid(self, pos, room):
        if (0 <= pos[0] < len(self.map) and 0 <= pos[1] < len(self.map[0]) and self.map[pos[0]][pos[1]] is None) or ((len(self.map)<=pos[0] or pos[0]<0) or (len(self.map[0])<=pos[1] or pos[1]<0)):
            if pos[0]+1 < len(self.map) and 0 <= pos[1] < len(self.map[0]) and self.map[pos[0]+1][pos[1]] is not None and self.map[pos[0]+1][pos[1]].doorways.count("north")>0 and room.doorways.count("south")>0:
                return True, "north"
            if pos[0]-1 >= 0 and 0 <= pos[1] < len(self.map[0]) and self.map[pos[0]-1][pos[1]] is not None and self.map[pos[0]-1][pos[1]].doorways.count("south")>0 and room.doorways.count("north")>0:
                return True, "south"
            if 0 <= pos[1]+1 < len(self.map[0]) and 0 <= pos[0] < len(self.map) and self.map[pos[0]][pos[1]+1] is not None and self.map[pos[0]][pos[1]+1].doorways.count("west")>0 and room.doorways.count("east")>0:
                return True, "west"
            if 0 <= pos[1]-1 < len(self.map[0]) and 0 <= pos[0] < len(self.map) and self.map[pos[0]][pos[1]-1] is not None and self.map[pos[0]][pos[1]-1].doorways.count("east")>0 and room.doorways.count("west")>0:
                return True, "east"
            return False, "none"
        else:
            return False, "none"

    #removes tiles from map (not cards as well)
    def remove_from_map(self, room):
        for x in range(len(self.map)):
            for l in range(len(self.map[x])):
                if self.map[x][l] == room:
                    self.map[x][l] = None
                    return True
        return False

# subject to change
    """
    def change_player_turn(self, players):
        if self.current_player+1 < len(players):
            self.current_player+=1
        else:
            self.current_player = 0

    def status(self):
        if

    def run_game(self):
        while(status() == 1):
    """

