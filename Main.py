import os, sys
import pygame, Game as g, MainFile as m
from pygame.locals import *
from tkinter import *

if not pygame.font: print
'Warning, fonts disabled'
if not pygame.mixer: print
'Warning, sound disabled'

"""
Import modules
set up game( difficulty  ) 
"""



# if pygame.font:
# font = pygame.font.Font(None, 50)
# text = font.render("Fire of Eidolon", 1 (10,10,10))
# textpos = text.get_rect(centerx = background.get_width()/2)
# background.blit(text,textpos)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except ValueError:
        print('Cannot load image:', name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect


def load_sound(name):
    return

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Fire of Eidolon')
    pygame.mouse.set_visible(1)

    backgroundImage = pygame.image.load("Textures/intro.png").convert()
    backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))
    screen.blit(backgroundImage, (0, 0))
    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    # background.fill((250,250,250))

    clock = pygame.time.Clock()
    done = False

    game = g.Game()
    graphics = m.MainFile

    while not done:

        done = game.process_events()

        game.logic()

        #graphics.update()

        clock.tick(60)


    pygame.quit()
    
hc = HeroesCards.HeroesCards
    heroes = hc.HeroList  # need to change to list of players

    card_scale = .6
    card_width = int(1149 * card_scale)
    card_height = int(749 * card_scale)

    turn = "Cleric"  # test value

    def draw_hero_list():
        mouse = pygame.mouse.get_pos()
        font = pygame.font.Font('freesansbold.ttf', 8)
        pygame.draw.rect(screen, (0, 0, 0), (20, 20, 60, 300))
        for i in range(len(heroes)):
            if Rect(25, i * 50 + 35, 40, 40).collidepoint(mouse):
                screen.blit(pygame.transform.scale(pygame.image.load("Textures/Heroes/" + heroes[i].type + ".jpg"),
                                                   (card_width, card_height)), [100, i * 50 + 35])
            if heroes[i].type == turn:
                pygame.draw.rect(screen, (100, 100, 100), (20, i * 50 + 25, 60, 50))
            screen.blit(pygame.transform.scale(pygame.image.load("Textures/CharacterImages/" + heroes[i].type + ".png"),
                                               (40, 40)), [25, i * 50 + 35])
            screen.blit(font.render(heroes[i].type, True, (255, 255, 255)), [25, i * 50 + 28])

if __name__ == "__main__":
    main()
