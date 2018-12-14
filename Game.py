# logic
import Cards as c, Room as r, Difficulty as d, HeroesCards as h

class Game:
    room_class = None
    map = []
    main_room = None
    current_player = None
    current_card_list = []
    current_deck = []
    void_deck = []
    difficulty_level = None
    player_list = []

    def __init__(self):
        self.room_class = r.Room()
        self.map = [[self.room_class.all_rooms.get("Vestibule")]]
        self.main_room = (0, 0)
        self.difficulty_level = d.All_Difficulties().difficulties.get("Normal") # random diff for now 
        self.player_list = [h.HeroesCards.aelfric, h.HeroesCards.cecilia, h.HeroesCards.tetemeko] # random players for now 
        self.current_player = self.player_list[0]
        self.map[0][0].players = self.player_list
        
    def player_actions(self, player, action, token):
        xPos = 0
        yPos = 0
        for x in range(len(self.map[0])):
            for i in range(len(self.map[1])):
                if self.map[x][i].players.contains(player):
                    current_tile = self.map[x][i]
                    xPos = x
                    yPos = i


        if self.current_player.amt_of_ap > 0:
            if action == 'w':
                if self.map[yPos + 1] > -1:
                    self.map[xPos][yPos + 1].players.append(player)


        # repeat for other keys
        if action == "pick_token" and current_tile.token != None:
            if current_tile.token == "green token":
                return 
                if self.current_player.amt_of_ap > 0:
            if action == 'w':
                if self.map[yPos + 1] > -1:
                    self.map[xPos][yPos + 1].players.append(player)

        # repeat for other keys
            if action == "collect_token" and current_tile.token != None:
                if current_tile.token == "key" and #(4 - self.current_player.amt_of_ap):
                    self.current_player

            if action == 'explore':
                pass
                #add new room if possible
            if action == 'attack' and current_tile.cultist != 0:
                current_tile.cultist -= 1
            if action == 'exchange' and len(current_tile.players) > 1:
                pass
                #add ui to exchange tokens
            if action == 'skill':
                #do player stuff
                pass
            if action == 'wait':
                #start cultist phase
                pass
            if action == "destroy_relic":
                pass
            if action == "retrieve_fire":
                pass

    #adds room tile to map
    def add_to_map(self, root_position, direction, room):
        if 0 <= root_position[0] < len(self.map) and 0 <= root_position[1] < len(self.map[0]):

            if direction == "north" and room.doorways.count("south") > 0:
                if root_position[0] == 0:
                    li = [None]*len(self.map[0])
                    li[root_position[1]] = room
                    self.map.insert(0, li)
                    self.main_room = (self.main_room[0]+1, self.main_room[1])
                elif self.map[root_position[0]-1][root_position[1]] is None:
                    self.map[root_position[0]-1][root_position[1]] = room
                    print(self.map)

            elif direction == "south" and room.doorways.count("north") > 0:
                if root_position[0] == len(self.map)-1:
                    li = [None]*len(self.map[0])
                    li[root_position[1]] = room
                    self.map.append(li)
                elif self.map[root_position[0]+1][root_position[1]] is None:
                    self.map[root_position[0]+1][root_position[1]] = room
                    print(self.map)

            elif direction == "west" and room.doorways.count("east") > 0:
                if root_position[1] == 0:
                    for x in range(len(self.map)):
                        if x == root_position[0]:
                            self.map[x].insert(0, room)
                        else:
                            self.map[x].insert(0, None)
                    self.main_room = (self.main_room[0], self.main_room[1]+1)
                elif self.map[root_position[0]][root_position[1]-1] is None:
                    self.map[root_position[0]][root_position[1]-1] = room
                    print(self.map)

            elif direction == "east" and room.doorways.count("west") > 0:
                if root_position[1] == len(self.map[0])-1:
                    for x in range(len(self.map)):
                        if x == root_position[0]:
                            self.map[x].append(room)
                        else:
                            self.map[x].append(None)
                elif self.map[root_position[0]][root_position[1]+1] is None:
                    self.map[root_position[0]][root_position[1]+1] = room
                    print(self.map)
        else:
            return False

    #removes tiles from map (not cards as well)
    def remove_from_map(self, room):
        for x in range(len(self.map)):
            for l in range(len(self.map[x])):
                if self.map[x][l] == room:
                    self.map[x][l] = None
                    return True
        return False

# subject to change
    def change_player_turn(self, players):
        if self.current_player+1 < len(players):
            self.current_player+=1
        else:
            self.current_player = 0

    def status(self):
        if

    def run_game(self):
        while(status() == 1):





g = Game()
print(g.map)
print(g.main_room)
