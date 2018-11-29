import pygame as pg, HeroesCards as Hc, Player as p
import os
from pygame.locals import *


class HeroesGraphics():
    select_button = False
    view_selected_hero = False
    num_buttons = False

    taken_image = 0
    taken_rect = 0

    num_o_heroes = 0
    run_number = 1

    pg.init()
    screen = pg.display.set_mode((1300,650))
    pg.display.set_caption('Heroes expand')
    pg.mouse.set_visible(1)

    my_font = pg.font.SysFont('Comic Sans MS', 25)
    text_surface1 = my_font.render('Hero Selection', False, (0, 0, 0))
    text_surface2 = my_font.render('How many players?', False, (0, 0, 0))
    text_surface3 = my_font.render('Go back', False, (0, 0, 0))
    text_surface4 = my_font.render('Choose this hero', False, (0,0,0))
    text_surface5 = my_font.render('Chosen Heroes', False, (0,0,0))

    Hero_List = Hc.HeroesCards.HeroList
    Num_O_Hero_Rect = []
    Rect_List = []
    Loaded_Image_List = []
    Chosen_Hero_Dict = {}
    Chosen_Hero_Image_List = []

    clock = pg.time.Clock()
    done = False

    for x in range(len(Hero_List)):
        Loaded_Image_List.append(Hc.HeroesCards.getImage(Hero_List[x].name))

    while not done:
        for event in pg.event.get():
            if event.type == QUIT:
                done = True
            if select_button == False:
                buttonRect = pg.Rect((550,275,200,100))
                pg.draw.rect(screen, (255,0,0), buttonRect)
                screen.blit(text_surface1,(565,300))
                if event.type == pg.MOUSEMOTION:
                    mx, my = event.pos
                    if buttonRect.collidepoint(mx, my):
                        pg.draw.rect(screen, (255,255,0), buttonRect)
                        screen.blit(text_surface1, (565, 300))
                if event.type == pg.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if buttonRect.collidepoint(mx, my):
                        pg.draw.rect(screen, (255, 255, 0), buttonRect)
                        screen.blit(text_surface1, (565, 300))
                        num_buttons = True
                if num_buttons == True:
                    screen.fill((0,0,0))
                    pg.draw.rect(screen,(255, 0, 0), pg.Rect((550,0,300,100)))
                    screen.blit(text_surface2, (575, 15))

                    for x in range(6):
                        pg.draw.rect(screen, (255, 0, 0), pg.Rect((x*250, 300, 50, 50)))
                        screen.blit(my_font.render(str(x+1), False, (0, 0, 0)),(x*255,300))
                        rect = pg.Rect((x*250, 300, 50, 50))
                        Num_O_Hero_Rect.append(rect)
                    if event.type == MOUSEMOTION:
                        mx, my = event.pos
                        for x in range(6):
                            if Num_O_Hero_Rect[x].collidepoint(mx, my):
                                pg.draw.rect(screen, (255, 255, 0), Num_O_Hero_Rect[x])
                                screen.blit(my_font.render(str(x+1), False, (0, 0, 0)), (x * 255, 300))
                    if event.type == MOUSEBUTTONDOWN:
                        mx, my = event.pos
                        for x in range(6):
                            if Num_O_Hero_Rect[x].collidepoint(mx, my):
                                pg.draw.rect(screen, (255, 255, 0), Num_O_Hero_Rect[x])
                                screen.blit(my_font.render(str(x+1), False, (0, 0, 0)), (x * 255, 300))
                                num_o_heroes = x+1
                                select_button = True
            elif select_button == True:
                if run_number<=num_o_heroes:
                    if view_selected_hero == False:
                        screen.fill((0, 0, 0))
                        screen.blit(my_font.render('Player '+str(run_number), False, (255, 255, 255)),(500,250))
                        for x in range(len(Hero_List)):
                            Loaded_Image = pg.transform.smoothscale(Loaded_Image_List[x], (200, 100))
                            if x < 6:
                                screen.blit(Loaded_Image, (1+x*220, 0))
                            elif x >= 6:
                                screen.blit(Loaded_Image, ((1 + x * 220) - 1320, 150))
                        Rect_List.clear()
                        for x in range(len(Hero_List)):
                            Loaded_Image = pg.transform.smoothscale(Loaded_Image_List[x], (200, 100))
                            if x < 6:
                                rect = Loaded_Image.get_rect()
                                rect = rect.move((1 + x * 220, 0))
                                Rect_List.append(rect)
                            elif x >= 6:
                                rect = Loaded_Image.get_rect()
                                rect = rect.move(((1 + x * 220) - 1320, 150))
                                Rect_List.append(rect)
                        if event.type == pg.MOUSEBUTTONDOWN:
                            mx, my = event.pos
                            for x in range(len(Rect_List)):
                                #print (Hero_List[x].name, "X: "+str(Rect_List[x].x), "Y: "+str(Rect_List[x].y), "Width: "+ str(Rect_List[x].w), "Height: "+ str(Rect_List[x].h), "Rect List Length: "+str(len(Rect_List)), "Index: "+str(x),"MouseX: "+str(mx),"MouseY: "+str(my))
                                if Rect_List[x].collidepoint(mx, my):
                                    view_selected_hero = True
                                    taken_rect = Rect_List[x]
                                    taken_image = Loaded_Image_List[x]
                                    break
                    if view_selected_hero == True:
                        #used for the expanding and deexpanding hero graphics
                        hold_taken_image = taken_image
                        used_taken_image = pg.transform.smoothscale(taken_image, (200, 100))

                        screen.fill((0,0,0))

                        buttonRect = pg.Rect((1000, 550, 300, 100))
                        pg.draw.rect(screen, (255, 0, 0), buttonRect)
                        screen.blit(text_surface3, (1050, 565))

                        buttonRect2 = pg.Rect((0, 550, 300, 100))
                        pg.draw.rect(screen, (255, 0, 0), buttonRect2)
                        screen.blit(text_surface4, (50, 565))

                        screen.blit(used_taken_image, (0,0))
                        taken_rect.x = 0
                        taken_rect.y = 0

                        if event.type == pg.MOUSEMOTION:
                            mx, my = event.pos
                            if buttonRect.collidepoint(mx, my):
                                pg.draw.rect(screen, (255, 255, 0), buttonRect)
                                screen.blit(text_surface3, (1050, 565))
                            elif buttonRect2.collidepoint(mx, my):
                                pg.draw.rect(screen, (255, 255, 0), buttonRect2)
                                screen.blit(text_surface4, (50, 565))
                            elif taken_rect.collidepoint(mx, my):
                                hold_taken_image = pg.transform.smoothscale(hold_taken_image, (822, 536))
                                screen.blit(hold_taken_image, (0, 0))
                            elif taken_rect.collidepoint(mx, my) == False:
                                screen.blit(used_taken_image, (0, 0))
                        if event.type == pg.MOUSEBUTTONDOWN:
                            mx, my = event.pos
                            if buttonRect.collidepoint(mx, my):
                                pg.draw.rect(screen, (255, 255, 0), buttonRect)
                                screen.blit(text_surface3, (1050, 565))
                                view_selected_hero = False
                            if buttonRect2.collidepoint(mx, my):
                                pg.draw.rect(screen, (255, 255, 0), buttonRect2)
                                screen.blit(text_surface4, (50, 565))

                                for x in range(len(Hero_List)):
                                    if Loaded_Image_List[x] == taken_image:
                                        Chosen_Hero_Dict['Player '+str(run_number)] = p.Player(Hero_List[x])
                                        print (Chosen_Hero_Dict['Player '+str(run_number)].hero.name)
                                        Chosen_Hero_Image_List.append(Loaded_Image_List[x])
                                        Hero_List.pop(x)
                                Loaded_Image_List.remove(taken_image)
                                view_selected_hero = False
                                run_number = run_number+1
                else:
                    screen.fill((0,0,0))
                    pg.draw.rect(screen, (255, 0, 0), pg.Rect((550, 0, 300, 100)))
                    screen.blit(text_surface5, (585, 15))

                    for x in range(len(Chosen_Hero_Dict)):
                        Chosen_Hero_Image_List[x] = pg.transform.smoothscale(Chosen_Hero_Image_List[x], (200, 100))
                        if x <= 2:
                            screen.blit(my_font.render('Player '+str(x+1)+":", False, (255, 255, 255)),(150+x*350,150))
                            screen.blit(Chosen_Hero_Image_List[x],(280 + x * 350, 140))
                        else:
                            screen.blit(my_font.render('Player ' + str(x + 1) + ":", False, (255, 255, 255)),((150 + x * 350)-1050, 300))
                            screen.blit(Chosen_Hero_Image_List[x],((280 + x * 350)-1050, 290))
                """if event.type == pg.MOUSEMOTION:
                    mx, my = event.pos
                    if heroImage.get_rect().collidepoint(mx,my):
                        heroImage = pg.transform.scale(heroImage, (300, 200))
                        screen.fill((0, 0, 0))
                        screen.blit(heroImage,(0,0))
                    else:
                        screen.fill((0, 0, 0))
                        heroImage = pg.transform.scale(heroImage, (200, 100))
                        screen.blit(heroImage, (0, 0))"""
            clock.tick(60)
            pg.display.update()
