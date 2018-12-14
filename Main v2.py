import os, sys, Cards, HeroesCards
import pygame
from pygame.locals import *
from tkinter import *

cards = Cards.Cards()


if not pygame.font: print
'Warning, fonts disabled'
if not pygame.mixer: print
'Warning, sound disabled'


#Import modules
#set up game( difficulty  )

display_width = 800
display_height = 600
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))#,pygame.FULLSCREEN)
pygame.display.set_caption('Fire of Eidolon')
pygame.mouse.set_visible(1)


backgroundImage = pygame.image.load("Textures/intro.png").convert()
backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))


cards.shuffle()
#screen.blit(cards.get_card_image(cards.current_deck[0]), (0, 0))


clock = pygame.time.Clock()
done = False

# if pygame.font:
# font = pygame.font.Font(None, 50)
# text = font.render("Fire of Eidolon", 1 (10,10,10))
# textpos = text.get_rect(centerx = background.get_width()/2)
# background.blit(text,textpos)

def load_sound(name):
    return


dark_grey = (120,120,120)
light_grey = (180,180,180)
current_buttons = {}
button_image = pygame.image.load("Textures/RPG_GUI_v1.png").convert_alpha()
button_a = pygame.Surface((291,62), pygame.SRCALPHA, 32).convert_alpha()
button_a.blit(button_image, (0,0), (10,123,291,62))
button_b = pygame.Surface((291,62), pygame.SRCALPHA, 32).convert_alpha()
button_b.blit(button_image, (0,0), (10,201,291,62))

"""def draw_button(rect, text, color): # dimension is (x,y,width,height)
    width = rect[2]
    height = rect[3]
    surf = pygame.Surface((width,height))
    pygame.draw.rect(surf, color, (0, 0, width, height))
    font = pygame.font.Font('freesansbold.ttf', 20)
    text_surf = font.render(text, False, (0, 0, 0))
    text_rect = text_surf.get_rect(center=(width / 2, height / 2))
    surf.blit(text_surf, text_rect)
    return surf
"""

def draw_button(rect,text,b): # dimension is (x,y,width,height)
    button = button_a.copy()
    if b:
        button = button_b.copy()
    font = pygame.font.Font('freesansbold.ttf', 20)
    text_surf = font.render(text, False, (0, 0, 0))
    text_rect = text_surf.get_rect(center=(291 / 2, 62 / 2))
    button.blit(text_surf, text_rect)
    return button

def interact_button(click):
    screen.blit(backgroundImage, (0, 0))
    mouse = pygame.mouse.get_pos()
    for key in current_buttons:
        rect = current_buttons[key]
        x = rect[0]
        y = rect[1]
        width = rect[2]
        height = rect[3]
        if Rect(x,y,width,height).collidepoint(mouse):
            screen.blit(draw_button(rect,key, True), (x,y))
            if click:
                if key == "Start":
                    draw_difficulty_screen()
                if key == "Quit":
                    sys.exit()
                if key == "Beginner":

                    pass
                break
        else:
            screen.blit(draw_button(rect, key, False),(x,y))

def draw_start():
    current_buttons.clear()
    current_buttons["Start"] = [250,200,291,62]
    current_buttons["Quit"] = [250, 300,291,62]


def draw_difficulty_screen():
    current_buttons.clear()
    current_buttons["Beginner"] = [100, 100,291,62]
    current_buttons["Normal"] = [100, 200, 291, 62]
    current_buttons["Hard"] = [100, 300, 291, 62]
    current_buttons["Very Hard"] = [100, 400, 291, 62]
    current_buttons["Extreme"] = [400, 100, 291, 62]
    current_buttons["Heroic"] = [400, 200, 291, 62]
    current_buttons["Nightmare"] = [400, 300, 291, 62]
    current_buttons["Legendary"] = [400, 400, 291, 62]

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

draw_start()

hc = HeroesCards.HeroesCards
heroes = hc.HeroList # need to change to list of players

card_scale = .6
card_width = int(1149*card_scale)
card_height = int(749*card_scale)

turn = "Cleric" # test value

def draw_hero_list():
    mouse = pygame.mouse.get_pos()
    font = pygame.font.Font('freesansbold.ttf', 8)
    pygame.draw.rect(screen, (0, 0, 0), (20, 20, 60, 300))
    for i in range(len(heroes)):
        if Rect(25, i*50+35, 40,40).collidepoint(mouse):
            screen.blit(pygame.transform.scale(pygame.image.load("Textures/Heroes/"+heroes[i].type+".jpg"),(card_width,card_height)), [100, i*50 + 35])
        if heroes[i].type == turn:
            pygame.draw.rect(screen,(100,100,100),(20, i*50 +25, 60 ,50))
        screen.blit(pygame.transform.scale(pygame.image.load("Textures/CharacterImages/"+heroes[i].type+".png"),(40,40)), [25, i*50 + 35])
        screen.blit(font.render(heroes[i].type, True,(255,255,255)),[25,i*50+28])


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

h=False

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        screen.blit(backgroundImage, (0, 0))
        if event.type == QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            interact_button(True)
        interact_button(False)
        if h:
            draw_hero_list()
    pygame.display.update()
    pygame.display.flip()