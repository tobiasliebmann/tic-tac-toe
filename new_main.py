import visualization as visu

import pygame as pg

import sys

my_game = visu.Graphics()
my_game.init_background()

while 1:
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos_x = pos[0]
            pos_y = pos[1]
            print(pos_x)
            print(pos_y)
            my_game.on_click(pos_x, pos_y)
            my_game.render_game()
            print(my_game.game_state.get_state_matrix())
    pg.display.flip()
