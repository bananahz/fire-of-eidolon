# logic
import Cards as c, Room as r, Difficulty as d, HeroesCards as h


class Game:
    room_class = None
    map = []
    main_room = None

    def __init__(self):
        self.room_class = r.Room()
        self.map = [[self.room_class.all_rooms.get("Vestibule")]]
        self.main_room = (0, 0)


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





g = Game()
print(g.map)
print(g.main_room)