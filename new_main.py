import visualization as visu

import pygame as pg

import sys

# pygame.init() is include in the __init__-function of Graphics
my_game = visu.Graphics()
my_game.init_visuals()

while 1:
    pos = pg.mouse.get_pos()
    my_game.check_visuals()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos_x = pos[0]
            pos_y = pos[1]
            my_game.on_click(pos_x, pos_y)
    pg.display.flip()
    if my_game.game_state.get_state_changed_flag():
        pg.time.delay(500)
    else:
        pg.time.delay(5)
