# logic
import pygame, Cards as c, Room as r, HeroesCards as h, Player as p


class Game:

    def __init__(self):

        self.game_over = False

        self.card_list = pygame.sprite.Group()
        self.room_list = pygame.sprite.Group()
        self.heroes_list = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            # mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def logic(self):
        if not self.game_over:
            self.all_sprites.update()

    def display_frame(self, screen):
        return
        # graphics
