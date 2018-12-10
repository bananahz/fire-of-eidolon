class Difficulty:
    def __init__(self, difficulty, levels):
        self.difficulty = difficulty
        self.current_draw_count = 0
        self.current_level = 0
        self.levels = levels
        self.link()

    def getCL(self):
        return self.current_level

    def getDif(self):
        return self.difficulty

    def curDC(self):
        return self.current_draw_count

    def get_levels(self):
        return self.levels

    def go_up(self):
        if self.current_level + 1 < len(self.levels):
            self.current_level += 1
            self.link()

    def link(self):
        self.current_draw_count = self.levels[self.current_level]


class All_Difficulties:
    def __init__(self):
        self.difficulties = {}
        self.load()

    def load(self):
        tFile = open("Difficulties.txt", 'r')
        lines = tFile.readlines()
        for x in range(len(lines)):
            items = lines[x].split(", ")
            level = None
            card_levels = None
            for y in range(len(items)):
                if y == 0:
                    level = items[y]
                else:
                    card_levels = []
                    count = items[y].split(":")
                    for c in count:
                        card_levels.append(int(c))
            self.difficulties[level] = Difficulty(level, card_levels)

    def get_all(self):
        return self.difficulties

# Difficulty Key_Words: Beginner, Normal, Hard, Very_Hard, Extreme, Heroic, Legendary, Nightmare

