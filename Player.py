import pygame, Hero as h


class Player(pygame.sprite.Sprite):

    def __init__(self, hero_name):
        self.hero = h.Hero.getImage(hero_name)
        # rect

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
