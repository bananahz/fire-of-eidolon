# logic
import Cards as c, Room as r, Difficulty as d, HeroesCards as h


class Game:
    room_class = None
    map = []
    main_room = None
    current_player = 0
    # temporary
    difficulty = None

    def __init__(self):
        self.room_class = r.Room()
        self.map = [[self.room_class.all_rooms.get("Vestibule")]]
        self.main_room = (0, 0)

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





g = Game()
print(g.map)
print(g.main_room)