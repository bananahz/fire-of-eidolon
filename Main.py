import os, sys
import pygame, Game as g, Difficulty as d, Cards as c
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
drawn_card = []
#heroesGraphics = hg.HeroesGraphics()

# button status
pressed = False
draw_button = False
placing_button = False
rotate_button = False

# set positions and scales for buttons and cards
dif_from_mouse = 0
shift_x = 350
shift_y = 250
scale_of_map = (100, 100)

# intro = hg.HeroesGraphics()
# player_list,difficulty = intrhero_Graphics()
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
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # intrhero_Graphics()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                event_manager_map(mouse_x, mouse_y, event)

        # heroesGraphics.hero_Graphics()
        # print(heroesGraphics.hero_Graphics()[0])
        # print(heroesGraphics.hero_Graphics()[1])
        screen.blit(backgroundImage, (0, 0))
        # draw_hero_list()
        draw_map()
        run_card_graphics()

        pygame.display.update()
        clock.tick(60)





#heroes = hc.HeroesCards.HeroList  # need to change to list of players

card_scale = .6
card_width = int(1149 * card_scale)
card_height = int(749 * card_scale)

turn = "Cleric"  # test value

"""
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
        """


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


def event_manager_map(mouse_x, mouse_y, event):
    global pressed
    global screen
    global draw_button
    global placing_button
    global rotate_button

    # set positions and scales for buttons and cards
    global dif_from_mouse
    global shift_x
    global shift_y
    global scale_of_map
    global drawn_card

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            pos = event.pos
            if 675 <= pos[0] <= 775 and 450 <= pos[1] <= 550:
                draw_button = True
            elif 550 <= pos[0] <= 560 and 435 <= pos[1] <= 445 and len(drawn_card) > 0:
                rotate_button = True
            elif 540 <= pos[0] <= 665 and 450 <= pos[1] <= 575 and len(drawn_card) > 0:
                placing_button = True
            else:
                pressed = True
                dif_from_mouse = shift_x - mouse_x, shift_y - mouse_y

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            pos = event.pos
            if 675 <= pos[0] <= 775 and 450 <= pos[1] <= 550 and len(game.room_class.current_deck) > 0 and len(
                    drawn_card) < 1:
                draw_button = False
                drawn_card = game.room_class.draw()

            elif 550 <= pos[0] <= 560 and 435 <= pos[1] <= 445 and len(drawn_card) > 0:
                rotate_button = False
                drawn_card[0].rotation()

            elif len(drawn_card) > 0 and placing_button and (
                    (540 > pos[0] or pos[0] > 665) or (450 > pos[1] or pos[1] > 575)):
                placing_button = False
                neg_y = 0
                neg_x = 0
                if ((mouse_y - shift_y) / 100) + game.main_room[0] < 0:
                    neg_y -= 1
                if ((mouse_x - shift_x) / 100) + game.main_room[1] < 0:
                    neg_x -= 1
                placed = game.add_to_map((neg_y + int(
                    ((mouse_y - shift_y) / 100) + game.main_room[0]), neg_x + int(
                    ((mouse_x - shift_x) / 100) + game.main_room[1])), drawn_card[0])
                if placed:
                    drawn_card = []
            else:
                pressed = False
                draw_button = False


def card_draw():
    global pressed
    global screen
    global draw_button
    global placing_button
    global rotate_button

    # set positions and scales for buttons and cards
    global dif_from_mouse
    global shift_x
    global shift_y
    global scale_of_map

    img = game.room_class.all_rooms.get("BackOfCard").image

    if len(game.room_class.current_deck) > 0:
        if draw_button:
            img = pygame.transform.smoothscale(img, (90, 90))
            screen.blit(img, (680, 455))
        else:
            img = pygame.transform.smoothscale(img, (100, 100))
            screen.blit(img, (675, 450))

    if len(drawn_card) != 0:
        draw = drawn_card[0].image
        draw = pygame.transform.smoothscale(draw, (125, 125))
        screen.blit(draw, (540, 450))
        pygame.draw.rect(screen, (255, 255, 255), (550, 435, 10, 10))


def draw_map():
    global pressed
    global screen
    global draw_button
    global placing_button
    global rotate_button

    # set positions and scales for buttons and cards
    global dif_from_mouse
    global shift_x
    global shift_y
    global scale_of_map

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if pressed and not draw_button:
        new_shift_x = dif_from_mouse[0] + mouse_x
        new_shift_y = dif_from_mouse[1] + mouse_y

        if 0 > (((len(game.map) - 1) - game.main_room[0]) * 100) + new_shift_y:
            shift_y = -(((len(game.map) - 1) - game.main_room[0]) * 100)
        elif ((0 - game.main_room[0]) * 100) + new_shift_y > 500:
            shift_y = 500 - ((0 - game.main_room[0]) * 100)
        else:
            shift_y = new_shift_y

        if 0 > (((len(game.map[0]) - 1) - game.main_room[1]) * 100) + new_shift_x:
            shift_x = -(((len(game.map[0]) - 1) - game.main_room[1]) * 100)
        elif ((0 - game.main_room[1]) * 100) + new_shift_x > 700:
            shift_x = 700 - ((0 - game.main_room[1]) * 100)
        else:
            shift_x = new_shift_x

    for y in range(len(game.map)):
        for x in range(len(game.map[y])):
            if game.map[y][x] is not None:
                img = game.map[y][x].image
                img = pygame.transform.smoothscale(img, (100, 100))
                screen.blit(img, (((x - game.main_room[1]) * 100) + shift_x,
                                          ((y - game.main_room[0]) * 100) + shift_y))

    card_draw()




if __name__ == "__main__":
    main()

