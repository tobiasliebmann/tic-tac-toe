import inspect

import button as bt

import pygame as pg

import sys


def exec_func(func_to_exec, *args):
    save_func = func_to_exec
    save_args = args
    return save_func(*save_args)


def my_add(a, b):
    return a + b


def my_func():
    print("Initializing black screen.")
    pg.display.set_mode((900, 900))


print(my_add(2, 3))
print(exec_func(my_add, 2, 3))
print(inspect.isfunction(my_add))

pg.init()

my_screen = pg.display.set_mode((900, 900))

my_button = bt.Button(my_func, my_screen, "I am a button, click me", "fonts/StandingRoomOnlyNF.ttf", 32,
                      (255, 0, 0), 450, 450)
my_button2 = bt.Button(my_func, my_screen, "I am a button, click me", "fonts/StandingRoomOnlyNF.ttf", 32,
                       (0, 255, 0), 450, 30)

my_button.draw_button()
my_button2.draw_button()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    my_button.listener()
    my_button2.listener()
    # Update the screen.
    pg.display.flip()
    pg.time.delay(5)
