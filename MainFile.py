# graphics
import Cards as c, Room as r, Difficulty as d, HeroesCards as h, pygame
from pygame.locals import *

My_red_color = (255, 0, 0)
My_blue_color = (0, 0, 255)
My_green_color = (0, 255, 0)


class MainFile():
    # map = {[r.Room.get_room_image(r, "Vestibule")]}  # scaled - new surface, 2d array
    room_deck = r.Room.current_deck
    difficulty = d.Difficulty
    cards = c.Cards.current_deck
    heroes = ""
    tokens = ""

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Fire of Eidolon')
    pygame.mouse.set_visible(1)

    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    # background.fill((250,250,250))

    clock = pygame.time.Clock()
    done = False

    # if pygame.font:
    # font = pygame.font.Font(None, 50)
    # text = font.render("Fire of Eidolon", 1 (10,10,10))
    # textpos = text.get_rect(centerx = background.get_width()/2)
    # background.blit(text,textpos)

    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True

        backgroundImage = pygame.image.load("Textures/intro.png").convert()
        backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))
        screen.blit(backgroundImage, (0, 0))

        #heroes
        pygame.draw.rect(screen, (0, 0, 0), (50, 100, 100, 100))
        pygame.draw.rect(screen, (0, 0, 0), (50, 250, 100, 100))
        pygame.draw.rect(screen, (0, 0, 0), (50, 400, 100, 100))

        #message
        pygame.draw.rect(screen, (0, 0, 0), (50, 550, 700, 40))

        #map
        pygame.draw.rect(screen, (0, 0, 0), (400, 200, 100, 100))


        #cards
        pygame.draw.rect(screen, (0, 0, 0), (650, 50, 100, 150))

        #stats
        pygame.draw.rect(screen, (0, 0, 0), (650, 300, 100, 200))

        pygame.display.flip()
