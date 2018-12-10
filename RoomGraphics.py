import Game as g, pygame as pg
from pygame.locals import *


class RoomGraphics:
    # button status
    pressed = False
    game_display = None
    draw_button = False
    placing_button = False
    rotate_button = False

    # set positions and scales for buttons and cards
    dif_from_mouse = 0
    shift_x = 350
    shift_y = 250
    scale_of_map = (100, 100)
    # format: (X position, Y position, scale of the X, scale of the Y)
    back_of_card_pos = (675, 450, 100, 100)
    drawn_card_pos = (540, 450, 125, 125)
    rotate_button_pos = (550, 435, 10, 10)

    # other
    game = None
    drawn_card = []

    def __init__(self):
        self.game_display = pg.display.set_mode((800, 600))
        self.game = g.Game()
        self.run_graphics()

    def event_manager(self, mouse_x, mouse_y):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = event.pos
                    if 675 <= pos[0] <= 775 and 450 <= pos[1] <= 550:
                        self.draw_button = True
                    elif 550 <= pos[0] <= 560 and 435 <= pos[1] <= 445 and len(self.drawn_card) > 0:
                        self.rotate_button = True
                    elif 540 <= pos[0] <= 665 and 450 <= pos[1] <= 575 and len(self.drawn_card) > 0:
                        self.placing_button = True
                    else:
                        self.pressed = True
                        self.dif_from_mouse = self.shift_x - mouse_x, self.shift_y - mouse_y
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    pos = event.pos

                    if 675 <= pos[0] <= 775 and 450 <= pos[1] <= 550 and len(self.game.room_class.current_deck) > 0 and len(self.drawn_card) < 1:
                        self.draw_button = False
                        self.drawn_card = self.game.room_class.draw()

                    elif 550 <= pos[0] <= 560 and 435 <= pos[1] <= 445 and len(self.drawn_card) > 0:
                        self.rotate_button = False
                        self.drawn_card[0].rotation()

                    elif len(self.drawn_card) > 0 and self.placing_button and ((540 > pos[0] or pos[0] > 665) or (450 > pos[1] or pos[1] > 575)):
                        self.placing_button = False
                        neg_y = 0
                        neg_x = 0
                        if ((mouse_y - self.shift_y)/100)+self.game.main_room[0] < 0:
                            neg_y -= 1
                        if ((mouse_x - self.shift_x)/100)+self.game.main_room[1] < 0:
                            neg_x -= 1
                        placed = self.game.add_to_map((neg_y + int(((mouse_y - self.shift_y)/100)+self.game.main_room[0]), neg_x + int(((mouse_x - self.shift_x)/100)+self.game.main_room[1])), self.drawn_card[0])
                        if placed:
                            self.drawn_card = []
                    else:
                        self.pressed = False
                        self.draw_button = False

    def card_draw(self):
        img = self.game.room_class.all_rooms.get("BackOfCard").image

        if len(self.game.room_class.current_deck) > 0:
            if self.draw_button:
                img = pg.transform.smoothscale(img, (90, 90))
                self.game_display.blit(img, (680, 455))
            else:
                img = pg.transform.smoothscale(img, (100, 100))
                self.game_display.blit(img, (675, 450))

        if len(self.drawn_card) != 0:
            draw = self.drawn_card[0].image
            draw = pg.transform.smoothscale(draw, (125,125))
            self.game_display.blit(draw, (540, 450))
            pg.draw.rect(self.game_display, (255,255,255), (550, 435, 10, 10))

    def run_graphics(self):
        while True:
            self.game_display.fill((0, 0, 0))
            mouse_x, mouse_y = pg.mouse.get_pos()

            self.event_manager(mouse_x, mouse_y)

            if self.pressed and not self.draw_button:
                new_shift_x = self.dif_from_mouse[0] + mouse_x
                new_shift_y = self.dif_from_mouse[1] + mouse_y

                if 0 > (((len(self.game.map) - 1) - self.game.main_room[0]) * 100) + new_shift_y:
                    self.shift_y = -(((len(self.game.map) - 1) - self.game.main_room[0]) * 100)
                elif ((0 - self.game.main_room[0]) * 100) + new_shift_y > 500:
                    self.shift_y = 500 - ((0 - self.game.main_room[0]) * 100)
                else:
                    self.shift_y = new_shift_y

                if 0 > (((len(self.game.map[0]) - 1) - self.game.main_room[1]) * 100) + new_shift_x:
                    self.shift_x = -(((len(self.game.map[0]) - 1) - self.game.main_room[1]) * 100)
                elif ((0 - self.game.main_room[1]) * 100) + new_shift_x > 700:
                    self.shift_x = 700 - ((0 - self.game.main_room[1]) * 100)
                else:
                    self.shift_x = new_shift_x

            for y in range(len(self.game.map)):
                for x in range(len(self.game.map[y])):
                    if self.game.map[y][x] is not None:
                        img = self.game.map[y][x].image
                        img = pg.transform.smoothscale(img, (100, 100))
                        self.game_display.blit(img, (((x - self.game.main_room[1]) * 100) + self.shift_x,
                                                     ((y - self.game.main_room[0]) * 100) + self.shift_y))

            self.card_draw()
            pg.display.update()

RoomGraphics()








