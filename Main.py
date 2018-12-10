import os, sys
import pygame, Game as g, HeroesGraphics as hg, Difficulty as d, HeroesCards as hc, Cards as c
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

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fire of Eidolon')
pygame.mouse.set_visible(1)

backgroundImage = pygame.image.load("Textures/intro.png").convert()
backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))
screen.blit(backgroundImage, (0, 0))

clock = pygame.time.Clock()
game = g.Game()
cards = c.Cards()
heroesGraphics = hg.HeroesGraphics()


# intro = hg.HeroesGraphics()
# player_list,difficulty = intro.hero_Graphics()
# print(player_list)
# print(difficulty)

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
    while True:
        # intro.hero_Graphics()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                heroesGraphics.hero_Graphics()
                print(heroesGraphics.hero_Graphics()[0])
                print(heroesGraphics.hero_Graphics()[1])
                screen.blit(backgroundImage, (0, 0))
                draw_hero_list()
                run_card_graphics()

                pygame.display.flip()
                clock.tick(60)


heroes = hc.HeroesCards.HeroList  # need to change to list of players

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


cards.load()
current_deck = cards.current_deck
current_card = current_deck.pop()
current_card_image = cards.get_card_image(current_card).convert()


def run_card_graphics():
    global current_card_image
    global current_deck
    global current_card
    pos = pygame.mouse.get_pos()

    card_pile = pygame.image.load("Textures/Cards/RitualCardBack.png").convert()
    card_pile = pygame.transform.scale(card_pile, ((int(card_pile.get_size()[0] * .2),
                                                    (int(card_pile.get_size()[1] * .2)))))
    card_pile_rect = card_pile.get_rect()
    card_pile_rect = card_pile_rect.move(650, 50)
    screen.blit(card_pile, (650, 50))

    current_card_image = pygame.transform.scale(current_card_image,
                                                (int(card_pile.get_size()[0]),
                                                 (int(card_pile.get_size()[1]))))
    screen.blit(current_card_image, (530, 50))

    if card_pile_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
        current_card = current_deck.pop()
        current_card_image = cards.get_card_image(current_card)
        print(len(current_deck))
        if len(cards.current_deck) == 0:
            current_deck = cards.current_deck
            print(len(cards.current_deck))


if __name__ == "__main__":
    main()

