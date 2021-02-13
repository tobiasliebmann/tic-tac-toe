import visualization as visu

import pygame as pg

import sys

# Inintialize verything.
# pygame.init() is include in the __init__-function of Graphics.
my_game = visu.Graphics()
my_game.init_visuals()

# Game loop.
while 1:
    # Check if the visuals correspond to the right state.
    my_game.check_visuals()
    # Check for events in the event que.
    for event in pg.event.get():
        # Check if the game was quit.
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # Check for mouse clicks.
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Save the position of the mouse at the moment the screen is clicked.
            pos_x, pos_y = pg.mouse.get_pos()
            my_game.on_click(pos_x, pos_y)
    # Update the screen.
    pg.display.flip()
    # If the game ended add a short delay
    if my_game.game_state.get_state_changed_flag():
        pg.time.delay(500)
    # If the game did not end, add a delay so that the CPU is occupied all the way.
    else:
        pg.time.delay(5)
